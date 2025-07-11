# gemini_auto_reply_email
### 概要
Gmailの未読メールを検知し，その未読メールをGeminiが返信を行ってくれるPythonプログラムです．

### バージョン
- Ubuntu 24.04.2 LTS
- Python 3.12.3

Pythonモジュール
- google-api-python-client 2.171.0
- google-auth-httplib2     0.2.0
- google-auth-oauthlib     1.2.2
- google-genai             1.20.0

### 実行方法
必要なモジュールのインストール
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install -q -U google-genai
```

1. Gmail APIの有効化
![image](https://github.com/user-attachments/assets/44213da2-d887-41bc-8458-1f0d0d8d95d0)

1. OAuth 2.0 クライアント IDの登録
![zu1](https://github.com/user-attachments/assets/bd992477-4606-4305-bbce-bab79ee84801)

1. Gemini API Keyの作成
![zu3](https://github.com/user-attachments/assets/faf42284-8b77-4e0c-ae62-0823566325d8)

1. credentials.jsonにGmail APIを有効化したプロジェクトのOAuth 2.0 クライアント IDのAPI Keyを貼り付ける．
1. reply_content.pyの`client = genai.Client(api_key="{gemini-api-key}")`にGeminiのAPI Keyを貼り付ける．
1. reply_content.pyの
```
response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"{text}"
    )
```
  に使用するモデルと，Geminiに送信する内容を入力する．（現在はモデルがgemini-2.0-flash，内容としてはメールの本文をそのままGeminiに送信している）
  
7. プログラムを実行する
```
python3 email-test.py
```

### 実行結果
1. URLが表示される
![image](https://github.com/user-attachments/assets/21a85f8c-7c93-4792-b7c5-99f0fbd82e60)

1. URL先に飛び，OAuth 2.0 クライアント IDの登録したアカウントを選択する
![458644045-3e0997bf-75cf-4282-9077-b2c2ccaae879](https://github.com/user-attachments/assets/dd2035f4-896d-4472-9cc8-aa26a19a536c)

1. アカウントにアクセス権限を与える
![458644268-f10b5450-b5f4-4176-bf99-f1c023627f18](https://github.com/user-attachments/assets/55fb36c1-0d04-4e3f-a29c-e5b257d737ba)

1. 出てきた認証コードをコピーし，貼り付ける
![458644403-d5553f1c-08f9-475a-ac9d-9b8e46022774](https://github.com/user-attachments/assets/4a270a0b-1638-4571-b8f4-de97d792931f)

1. Geminiから返信が返ってくる

送信したメール
![458645716-29f0c9dc-50a1-4367-b6fc-13087b5701f6](https://github.com/user-attachments/assets/ce977a99-02b1-4e37-ac8e-406740331627)

返信されたメール
![image](https://github.com/user-attachments/assets/ed939bbb-c975-45be-a373-c5c3817d9f63)



