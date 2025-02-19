import os
import requests
from dotenv import load_dotenv
import time
from datetime import datetime
from utils.extract_check_in_out import is_latest_end_of_line_log_about_check_in_out_java_edition, is_log_updated, return_about_check_in_out_java_edition, update_latest_added_lines_log, update_latest_end_of_line_log, update_check_in_out_log, extract_online_players, is_added_log_about_check_in_out
from utils.helpers import is_empty

# .env を読み込む
load_dotenv()

# Webhook URL を環境変数から取得
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
DISCORD_LOG_CHANNNEL_WEBHOOK_URL = os.getenv("DISCORD_LOG_CHANNNEL_WEBHOOK_URL")
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("DISCORD_MINECRAFT_CHANNEL_ID")

# print(DISCORD_WEBHOOK_URL)


def send_discord_message(message, URL):
    """引数で受け取ったURLのチャンネルにメッセージを送信"""
    payload = {"content": message}
    response = requests.post(URL, json=payload)

    if response.status_code == 204:
        print("✅ メッセージ送信成功！")
    else:
        print(f"❌ 送信エラー: {response.status_code}, {response.text}")


def update_latest_changed_log():
    """
    取得したlatest.logから変更箇所を更新(抽出)する関数
    """
    # if is_log_updated():

    update_latest_added_lines_log()  # latest.logに追加された行の更新
    update_latest_end_of_line_log()  # latest.logの末尾の行の更新


def send_discord_message_about_check_in_out():
    """
    Discordに入退室に関するメッセージを送信する関数
    """
    with open("src/data/output/latest_added_lines.log", 'r')as file:
        latest_added_lines_data = file.read()
        latest_added_lines_data = latest_added_lines_data.split("\n")
    messages = return_about_check_in_out_java_edition(latest_added_lines_data)

    for message in messages:
        send_discord_message(message, DISCORD_WEBHOOK_URL)


def send_discord_message_about_added_latest_log():
    """
    Discordにlatest.logメッセージを送信する関数
    """
    with open("src/data/output/latest_added_lines.log", 'r')as file:
        latest_added_lines_data = file.read()
        # latest_added_lines_data = latest_added_lines_data.split("\n")
    # messages = return_about_check_in_out_java_edition(latest_added_lines_data)
    if is_empty(latest_added_lines_data):
        print("latest.log に変更はありません")
    else:
        send_discord_message(latest_added_lines_data, DISCORD_LOG_CHANNNEL_WEBHOOK_URL)


def update_channel_topic():
    """Discordのチャンネルトピックを変更する関数(表示させるトピック: オンラインのプレイヤーの名前)
    """

    new_topic = "オンラインのプレイヤー: "
    online_players, offline_players = extract_online_players()

    for oneline_player in online_players:
        new_topic += oneline_player + ", "

    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "topic": new_topic
    }

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print("チャンネルトピックを更新しました．")
    elif response.status_code == 429:
        retry_after = response.json().get("retry_after", 30)  # 待機時間を取得
        print(f"チャンネル操作のリミットに達しました． retry_after = {retry_after}")
        print(response.status_code, response.json())
        # time.sleep(retry_after)
    else:
        print(response.status_code, response.json())


def update_channel_name():
    """Discordのチャンネル名を名前+オンラインに変更する関数
    """

    online_players, offline_players = extract_online_players()
    new_name = f"minecraft🔥{len(online_players)}"

    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "name": new_name
    }

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print("チャンネル名を更新しました．")
    elif response.status_code == 429:
        retry_after = response.json().get("retry_after", 30)  # 待機時間を取得
        print(f"チャンネル操作のリミットに達しました． retry_after = {retry_after}")
        print(response.status_code, response.json())
        # time.sleep(retry_after)
    else:
        print(response.status_code, response.json())


def print_debug_logs():
    print("--- DEBUG LOGS ----------")
    online_players, offline_players = extract_online_players()
    print("online_players:", online_players)
    print("offline_players:", offline_players)


if __name__ == "__main__":
    now = datetime.now()

    update_latest_changed_log()
    update_check_in_out_log()
    extract_online_players()

    send_discord_message_about_check_in_out()
    send_discord_message_about_added_latest_log()

    if is_added_log_about_check_in_out():
        update_channel_name()
        update_channel_topic()

    print_debug_logs()
