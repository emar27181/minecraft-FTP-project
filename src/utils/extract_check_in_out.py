def extract_check_in_out():
    """
      latest.logから入退室に関する情報を抽出する関数
    """
    with open("src/data/output/latest.log", 'r')as file:
        log_data = file.read()

    log_data = log_data.split('\n')

    for log in log_data:
        # 接続・切断に関するログだった場合
        if "connect" in log:
            splited_log = log.split(" ")
            date, time, connection, player_name, xuid = splited_log[0], splited_log[1], splited_log[4], splited_log[5], splited_log[7]

            player_name = player_name.strip(",")

            # print(f"{date} {time} {connection} {player_name}")
            if (connection == "disconnected"):
                print(f" {player_name} が退出しました．")
            else:
                print(f" {player_name} が入室しました．")


def is_log_updated():
    """
      latest.logの最終行から新しいログが追加されたか確認する関数

    引数: 
        None

    戻り値:
        bool: 新しいログがある場合True，無い場合False

    """
    with open("src/data/output/latest.log", 'r')as file:
        latest_log_data = file.read()

    with open("src/data/output/latest_end_of_line.log", 'r')as file:
        latest_end_of_line_log_data = file.read()

    latest_log_data = latest_log_data.split('\n')
    now_end_of_line_log_data = latest_log_data[len(latest_log_data) - 2]  # ログの末尾は空行なので，-2で最終行末尾を取得

    # 現在の末尾のログのが前回の末尾のログと同じ場合
    if (now_end_of_line_log_data == latest_end_of_line_log_data):
        print(f"=== 新しいログはありません．=============\n{latest_end_of_line_log_data} ⇔ {now_end_of_line_log_data}")
        return False

    # 現在の末尾のログのが前回の末尾のログと異なる場合
    else:
        print(f"=== 新しいログがあります．=============\n{latest_end_of_line_log_data} -> {now_end_of_line_log_data}")
        with open("src/data/output/latest_end_of_line.log", "w", encoding="utf-8") as f:
            f.write(now_end_of_line_log_data)
        return True

    # print(latest_log_data)


if __name__ == '__main__':

    if is_log_updated():
        extract_check_in_out()
