# CSV 轉 Excel
df = pd.read_csv("data.csv")
df.to_excel("data.xlsx", index=False)
print("CSV 轉換為 Excel 完成")

# JSON 轉 Excel
df = pd.read_json("data.json")
df.to_excel("data.xlsx", index=False)
print("JSON 轉換為 Excel 完成")
