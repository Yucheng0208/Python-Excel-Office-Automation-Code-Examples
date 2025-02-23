import pandas as pd

df = pd.read_excel("季業績資料 4.xlsx", sheet_name="業務部")

# 新增總業績與平均業績欄位
df["總業績"] = df.iloc[:, 1:].sum(axis=1)
df["平均業績"] = df.iloc[:, 1:-1].mean(axis=1)

df.to_excel("季業績資料 5.xlsx", index=False, sheet_name="業務部")
print("已儲存為 季業績資料 5.xlsx")
