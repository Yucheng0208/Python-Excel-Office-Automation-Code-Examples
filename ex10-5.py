import os

path = "ch10"
for root, dirs, files in os.walk(path):
    print("目錄:", root)
    print("子目錄:", dirs)
    print("檔案:", files)
