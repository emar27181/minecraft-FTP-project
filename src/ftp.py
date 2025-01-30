from ftplib import FTP
from dotenv import load_dotenv
import os
from datetime import datetime


# 環境変数を取得，変数の初期化
load_dotenv()
ftp_host = os.getenv("FTP_HOST")
ftp_port = int(os.getenv("FTP_PORT"))
ftp_user = os.getenv("FTP_USER")
ftp_pass = os.getenv("FTP_PASS")
ftp = FTP()


def download_file(dir_path, filename):
    """指定されたパスのファイルをダウンロードする関数

    引数:
        dir_path (str): ダウンロードするディレクトリパス
        filename (str): ダウウンロードしたファイルの保存名

    戻り値:
        None
    """
    ftp.cwd(dir_path)  # ディレクトリに移動
    output_file_path = f"src/data/output/{filename}"

    # latest.logをダウンロード
    with open(output_file_path, "wb") as f:
        ftp.retrbinary("RETR latest.log", f.write)

    now = datetime.now()

    print(f"latest.log をダウンロードしました．({now})\n path: {output_file_path}")


def run_ftp_connection():
    """
    FTP通信を実行する関数
    """
    try:
        # FTPサーバーに接続
        # ftp = FTP()
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_user, ftp_pass)

        print("=== FTP接続成功 =================")

        # 現在のディレクトリの一覧を取得
        files = ftp.nlst()
        # print("ファイル一覧:", files)

        download_file("/minecraft/logs/", "latest.log")
        # download_file("/minecraft/worlds/", "worlds")

        # 接続終了
        ftp.quit()

    except Exception as e:
        print("FTP接続エラー:", e)


if __name__ == "__main__":
    run_ftp_connection()
