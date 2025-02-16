def return_about_check_in_out_one_line_be_edition(log_line):
    """
      引数で受け取ったログに入退室に関する表示文を返す関数(統合版用)

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


def return_about_check_in_out_java_edition(log_lines):
    """
      引数で受け取ったログのうち入退室に関する表示文を返す関数(Java版用)

    引数:
        log_lines (list): ログ

    戻り値:
        about_check_in_out_lines: 入退室に関する表示文をリストで返す
    """

    about_check_in_out_lines = []
    for log_line in log_lines:
        if (is_log_about_check_in_out_java_edition(log_line)):
            about_check_in_out_lines.append(return_about_check_in_out_one_line_java_edition(log_line))

    return about_check_in_out_lines


def return_about_connection_data_from_log_line(log_line):
    """
    引数で受け取ったログからプレイヤー名と接続状態を抽出する関数

    引数:
        log_line (str): 入退室に関するログ

    戻り値:
        time (str): 時刻
        player_name (str): プレイヤー名
        connection (str): 接続状態
    """

    splited_log = log_line.split(" ")
    time, player_name, connection = splited_log[0], splited_log[3], splited_log[4]
    return time, player_name, connection


def return_about_check_in_out_one_line_java_edition(log_line):
    """
    引数で受け取ったログに入退室に関する表示文を返す関数(Java版用)

    引数:
        log_line (str): 入退室に関するログ

    戻り値:
        str: 入退室に関する表示文
    """

    splited_log = log_line.split(" ")
    time, player_name, connection = splited_log[0], splited_log[3], splited_log[4]

    if (connection == "left"):
        print(f" {player_name} が退出しました．")
        return f" {player_name} が退出しました．"
    else:
        print(f" {player_name} が入室しました．")
        return f" {player_name} が入室しました．"


def update_latest_added_lines_log():
    """更新されたlatest.logの追記個所を抽出する関数(抽出される行数>=1)
    """

    with open("src/data/output/latest.log", 'r')as file:
        latest_log_data = file.read()
        latest_log_data = latest_log_data.split('\n')
        now_end_of_line_log_data = latest_log_data[len(latest_log_data) - 2]  # ログの末尾は空行なので，-2で最終行末尾を取得

    with open("src/data/output/latest_end_of_line.log", 'r')as file:
        latest_end_of_line_log_data = file.read()

    added_lines = []
    for latest_log_one_line in reversed(latest_log_data):
        if (latest_log_one_line != latest_end_of_line_log_data):
            added_lines.append(latest_log_one_line)
        else:
            break

    added_lines.reverse()

    output_file_path = "src/data/output/latest_added_lines.log"
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(added_lines))
    print(f"{output_file_path} を更新しました．")


def update_latest_end_of_line_log():
    """latest.logの末尾の行を更新する関数
    """

    with open("src/data/output/latest.log", 'r')as file:
        latest_log_data = file.read()
        latest_log_data = latest_log_data.split('\n')
        now_end_of_line_log_data = latest_log_data[len(latest_log_data) - 2]  # ログの末尾は空行なので，-2で最終行末尾を取得

    output_file_path = "src/data/output/latest_end_of_line.log"

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(now_end_of_line_log_data)

    print(f"{output_file_path} を更新しました．")


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
        return True


def is_log_about_check_in_out_java_edition(log_line):
    """
        引数で受け取った行が入退室に関するログか確認する関数(Java用)

    引数:
        None

    戻り値:
        bool: 入退室に関するログの場合True，そうでない場合False

    """

    return "the game" in log_line


def is_latest_end_of_line_log_about_check_in_out_be_edition():
    """
        latest_end_of_line.logの最終行が入退室に関するログか確認する関数(統合版(BE)用)

    引数:
        None

    戻り値:
        bool: 入退室に関するログの場合True，そうでない場合False

    """
    with open("src/data/output/latest_end_of_line.log", 'r')as file:
        latest_end_of_line_log_data = file.read()

    return "Player" in latest_end_of_line_log_data


def is_latest_end_of_line_log_about_check_in_out_java_edition():
    """
        latest_end_of_line.logの最終行が入退室に関するログか確認する関数(Java用)

    引数:
        None

    戻り値:
        bool: 入退室に関するログの場合True，そうでない場合False

    """
    with open("src/data/output/latest_end_of_line.log", 'r')as file:
        latest_end_of_line_log_data = file.read()

    return "the game" in latest_end_of_line_log_data
