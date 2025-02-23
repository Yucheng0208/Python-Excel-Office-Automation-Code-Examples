file_path = input("請輸入程式碼檔案路徑: ")
output_path = "output.txt"

with open(file_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for idx, line in enumerate(infile, start=1):
        outfile.write(f"{idx:02d}: {line}")
print(f"已輸出至 {output_path}")