import pandas as pd

df1 = pd.read_excel("ch13/文具商品採購 2/文具商品採購清單_財務部.xlsx")
df2 = pd.read_excel("ch13/文具商品採購 2/文具商品採購清單_採購部.xlsx")

df_all = pd.concat([df1, df2])
df_all.to_excel("ch13/文具商品採購_分析.xlsx", index=False)

print("已建立 文具商品採購_分析.xlsx")
