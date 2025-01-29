def extract_check_in_out():
  """
    latest.logから入退室に関する情報を抽出する関数
  """
  with open("src/data/output/latest.log", 'r')as file:
    data = file.read()
    print(data)
  
if __name__ == '__main__':
  extract_check_in_out()