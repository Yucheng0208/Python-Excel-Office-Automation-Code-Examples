from pathlib import Path

file_path = "emails.txt"

# 讀取文件內容並顯示
with open(file_path, "r", encoding="utf-8") as file:
    emails = file.readlines()

print("電子郵件清單:")
for email in emails:
    print(email.strip())
