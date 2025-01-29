def extract_check_in_out():
  """
    latest.logから入退室に関する情報を抽出する関数
  """
  with open("src/data/output/latest.log", 'r')as file:
    log_data = file.read()
    
  log_data = log_data.split('\n')
  
  for log in log_data:
    if "connect" in log :
      if "disconnect" in log:
        print("disconnect")
        
      else:
        print("connect")
  
if __name__ == '__main__':
  extract_check_in_out()