# gemini_auto_reply_email
### 概要
未読メールを検知し，その未読メールをGeminiが返信を行ってくれるPythonプログラムです．

### バージョン
- Ubuntu 24.04.2 LTS
- Python 3.12.3

Pythonモジュール
- annotated-types          0.7.0
- anyio                    4.9.0
- cachetools               5.5.2
- certifi                  2025.4.26
- charset-normalizer       3.4.2
- google-api-core          2.25.0
- google-api-python-client 2.171.0
- google-auth              2.40.2
- google-auth-httplib2     0.2.0
- google-auth-oauthlib     1.2.2
- google-genai             1.20.0
- googleapis-common-protos 1.70.0
- h11                      0.16.0
- httpcore                 1.0.9
- httplib2                 0.22.0
- httpx                    0.28.1
- idna                     3.10
- oauthlib                 3.2.2
- pip                      24.0
- proto-plus               1.26.1
- protobuf                 6.31.1
- pyasn1                   0.6.1
- pyasn1_modules           0.4.2
- pydantic                 2.11.7
- pydantic_core            2.33.2
- pyparsing                3.2.3
- requests                 2.32.3
- requests-oauthlib        2.0.0
- rsa                      4.9.1
- sniffio                  1.3.1
- typing_extensions        4.14.0
- typing-inspection        0.4.1
- uritemplate              4.2.0
- urllib3                  2.4.0
- websockets               15.0.1

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
![image](https://github.com/user-attachments/assets/3e0997bf-75cf-4282-9077-b2c2ccaae879)

1. アカウントにアクセス権限を与える
![image](https://github.com/user-attachments/assets/f10b5450-b5f4-4176-bf99-f1c023627f18)

1. 出てきた認証コードをコピーし，貼り付ける
![458644403-d5553f1c-08f9-475a-ac9d-9b8e46022774](https://github.com/user-attachments/assets/4a270a0b-1638-4571-b8f4-de97d792931f)

1. Geminiから返信が返ってくる
送信したメール
![image](https://github.com/user-attachments/assets/29f0c9dc-50a1-4367-b6fc-13087b5701f6)

返信されたメール
![image](https://github.com/user-attachments/assets/ed939bbb-c975-45be-a373-c5c3817d9f63)



