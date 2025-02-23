import pandas as pd

data = {
    "月份": ["一月", "二月"],
    "網路商店": [35, 24],
    "實體店面": [25, 43]
}

df = pd.DataFrame(data)
df.to_excel("季業績資料.xlsx", index=False, sheet_name="業務部")
print("已建立季業績資料.xlsx")
