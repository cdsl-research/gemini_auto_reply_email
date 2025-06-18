# reply_content.py

import re
from google import genai

def gemini(text):
    # Gemini APIによって返信
    client = genai.Client(api_key="{gemini-api-key}")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"{text}"
    )

    return response.text

def get_reply(subject_in, body_in):
    subject_out = f"Re: {subject_in}"

    # マスク処理した本文をgeminiで返信してもらう
    ai_body = gemini(body_in)

    body_out = (
        "お問い合わせありがとうございます。\n\n"
        "こちらは自動返信です\n"
        "----------------------------------------\n"
        f"{ai_body}\n"
        "----------------------------------------\n\n"
    )
    return subject_out, body_out
