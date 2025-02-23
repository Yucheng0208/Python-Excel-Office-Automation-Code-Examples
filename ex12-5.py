df = pd.read_excel("季業績資料 3.xlsx", sheet_name="業務部")

# 修改二月的數據
df.loc[df["月份"] == "二月", "網路商店"] = 26
df.loc[df["月份"] == "二月", "業務直銷"] = 30
df.loc[df["月份"] == "三月", "實體店面"] = 35

df.to_excel("季業績資料 4.xlsx", index=False, sheet_name="業務部")
print("已儲存為 季業績資料 4.xlsx")
