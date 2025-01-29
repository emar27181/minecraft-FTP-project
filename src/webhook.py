import os
import requests
from dotenv import load_dotenv

# .env を読み込む
load_dotenv()

# Webhook URL を環境変数から取得
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

print(DISCORD_WEBHOOK_URL)

def send_discord_message(message):
    """Discord にメッセージを送信"""
    payload = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        print("✅ メッセージ送信成功！")
    else:
        print(f"❌ 送信エラー: {response.status_code}, {response.text}")

# "HelloWorld" を送信
send_discord_message("HelloWorld")
