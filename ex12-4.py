df = pd.read_excel("季業績資料 2.xlsx", sheet_name="業務部")
df.loc[len(df)] = ["三月", 15, 32, 12]
df.to_excel("季業績資料 3.xlsx", index=False, sheet_name="業務部")
print("已儲存為 季業績資料 3.xlsx")