import os
import requests
from dotenv import load_dotenv
from utils.extract_check_in_out import is_latest_end_of_line_log_about_check_in_out_java_edition, is_log_updated, return_about_check_in_out_java_edition, update_latest_added_lines_log, update_latest_end_of_line_log

# .env を読み込む
load_dotenv()

# Webhook URL を環境変数から取得
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# print(DISCORD_WEBHOOK_URL)


def send_discord_message(message):
    """Discord にメッセージを送信"""
    payload = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

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
    Discordにメッセージを送信する関数
    """
    with open("src/data/output/latest_added_lines.log", 'r')as file:
        latest_added_lines_data = file.read()
        latest_added_lines_data = latest_added_lines_data.split("\n")
    messages = return_about_check_in_out_java_edition(latest_added_lines_data)

    for message in messages:
        print(message)
    # print(f"latest_added_lines_data = {latest_added_lines_data}")


if __name__ == "__main__":

    # print(is_send_discord_message_about_check_in_out())

    update_latest_changed_log()
    send_discord_message_about_check_in_out()
    """
    if (send_discord_message_about_check_in_out()):
        with open("src/data/output/latest_end_of_line.log", 'r')as file:
            latest_end_of_line_log_data = file.read()
        # send_discord_message(return_about_check_in_out_java_edition(latest_end_of_line_log_data))
    # send_discord_message("HelloWorld")
    """
