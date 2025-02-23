df = pd.read_excel("季業績資料.xlsx", sheet_name="業務部")
df["業務直銷"] = [33, 25]
df.to_excel("季業績資料 2.xlsx", index=False, sheet_name="業務部")
print("已儲存為 季業績資料 2.xlsx")