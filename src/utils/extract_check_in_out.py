def return_about_check_in_out(log_line):
    """
      引数で受け取ったログに入退室に関する表示文を返す関数

    引数:
        log_line (str): 入退室に関するログ

    戻り値:
        str: 入退室に関する表示文
    """

    splited_log = log_line.split(" ")
    date, time, connection, player_name, xuid = splited_log[0], splited_log[1], splited_log[4], splited_log[5], splited_log[7]

    player_name = player_name.strip(",")
    connection = connection.strip(":")

    if (connection == "disconnected"):
        print(f" {player_name} が退出しました．")
        return f" {player_name} が退出しました．"
    else:
        print(f" {player_name} が入室しました．")
        return f" {player_name} が入室しました．"


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


def is_latest_end_of_line_log_about_check_in_out():
    """
        latest_end_of_line.logの最終行が入退室に関するログか確認する関数

    引数:
        None

    戻り値:
        bool: 入退室に関するログの場合True，そうでない場合False

    """
    with open("src/data/output/latest_end_of_line.log", 'r')as file:
        latest_end_of_line_log_data = file.read()

    return "Player" in latest_end_of_line_log_data
