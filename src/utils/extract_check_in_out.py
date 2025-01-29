def extract_check_in_out():
  """
    latest.logから入退室に関する情報を抽出する関数
  """
  with open("src/data/output/latest.log", 'r')as file:
    log_data = file.read()
    
  log_data = log_data.split('\n')
  
  for log in log_data:
    # 接続・切断に関するログだった場合
    if "connect" in log :
      splited_log = log.split(" ")
      date,time, connection, player_name, xuid = splited_log[0], splited_log[1], splited_log[4], splited_log[5], splited_log[7]
      
      player_name = player_name.strip(",")
      
      # print(f"{date} {time} {connection} {player_name}")
      if (connection == "disconnected"):
        print(f" {player_name} が退出しました．")
      else :
        print(f" {player_name} が入室しました．")
      
  
if __name__ == '__main__':
  extract_check_in_out()