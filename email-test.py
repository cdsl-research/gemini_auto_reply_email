import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.text import MIMEText
from apiclient import errors

from reply_content import get_reply

# 1. Gmail APIのスコープを設定
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
# 2. メール本文の作成
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    encode_message = base64.urlsafe_b64encode(message.as_bytes())
    return {'raw': encode_message.decode()}
# 3. メール送信の実行
def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
# 4. メインとなる処理
def main():
    # 5. アクセストークンの取得
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # CLI対応の認証手順（ブラウザ不要）
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
            auth_url, _ = flow.authorization_url(prompt='consent')

            print("\n以下のURLをブラウザで開いて、Googleアカウントでログインし、表示された認可コードをコピーしてください：\n")
            print(auth_url)
            code = input("\n認可コードをここに貼り付けてください：\n> ")
            flow.fetch_token(code=code)
            creds = flow.credentials
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    # 6. 未読メールを取得して自動返信
    results = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD']).execute()
    messages = results.get('messages', [])

    if not messages:
        print("未読メールはありません。")
        return

    for m in messages:
        msg = service.users().messages().get(userId='me', id=m['id'], format='full').execute()
        headers = msg['payload']['headers']
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        subject_in = next((h['value'] for h in headers if h['name'] == 'Subject'), '(件名なし)')

        body_in = ""
        parts = msg['payload'].get('parts', [])
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                body_in = base64.urlsafe_b64decode(data).decode('utf-8')
                break

        # 件名と本文を動的に生成
        subject_out, body_out = get_reply(subject_in, body_in)

        message = create_message(sender, sender, subject_out, body_out)


        # メールを送信
        send_message(service, 'me', message)

        # メールを既読に変更
        service.users().messages().modify(userId='me', id=m['id'], body={'removeLabelIds': ['UNREAD']}).execute()

        print(f" {sender} に返信しました。")

# 8. プログラム実行！
if __name__ == '__main__':
    main()
