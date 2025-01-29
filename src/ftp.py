from ftplib import FTP
from dotenv import load_dotenv
import os

# .env を読み込む
load_dotenv()

# 環境変数を取得
ftp_host = os.getenv("FTP_HOST")
ftp_port = int(os.getenv("FTP_PORT"))
ftp_user = os.getenv("FTP_USER")
ftp_pass = os.getenv("FTP_PASS")

try:
    # FTPサーバーに接続
    ftp = FTP()
    ftp.connect(ftp_host, ftp_port)
    ftp.login(ftp_user, ftp_pass)
    
    print("=== FTP接続成功 =================")
    
    # 現在のディレクトリの一覧を取得
    files = ftp.nlst()
    # print("ファイル一覧:", files)
    
    
    # `logs` ディレクトリに移動
    ftp.cwd("/minecraft/logs/")
    output_file_path = "src/data/output/latest.log"

    # latest.logをダウンロード
    with open(output_file_path, "wb") as f:
        ftp.retrbinary("RETR latest.log", f.write)

    print(f"latest.log をダウンロードしました．\n path: {output_file_path}")

    # 接続終了
    ftp.quit()

except Exception as e:
    print("FTP接続エラー:", e)
    

