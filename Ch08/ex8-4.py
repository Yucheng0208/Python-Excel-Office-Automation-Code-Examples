file_path = input("請輸入檔案路徑: ")
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())
