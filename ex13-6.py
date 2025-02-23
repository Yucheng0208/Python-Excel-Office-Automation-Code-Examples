import os
import pandas as pd

os.makedirs("ch13/文具商品採購 2", exist_ok=True)

df1 = pd.DataFrame({"品名": ["鉛筆", "橡皮擦"], "數量": [10, 5]})
df2 = pd.DataFrame({"品名": ["筆記本", "文件夾"], "數量": [7, 3]})

df1.to_excel("ch13/文具商品採購 2/文具商品採購清單_財務部.xlsx", index=False)
df2.to_excel("ch13/文具商品採購 2/文具商品採購清單_採購部.xlsx", index=False)

print("已建立 Excel 文件")
