import schedule
import time
import subprocess


# 1分おきにFTP接続を行い，latest.logをダウンロードする関数


def run_script():
    print("Executing run.py...")
    subprocess.run(["python", "src/ftp.py"])


schedule.every(1).minutes.do(run_script)

if __name__ == "__main__":
    subprocess.run(["python", "src/ftp.py"])

    while True:
        schedule.run_pending()
        time.sleep(1)
