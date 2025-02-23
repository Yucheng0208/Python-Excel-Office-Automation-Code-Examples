df = pd.read_excel("季業績資料 5.xlsx", sheet_name="業務部")

# 新增通路總業績與平均
df.loc["總計"] = df.iloc[:, 1:].sum()
df.loc["平均"] = df.iloc[:-1, 1:].mean()

df.to_excel("季業績資料 6.xlsx", index=False, sheet_name="業務部")
print("已儲存為 季業績資料 6.xlsx")
