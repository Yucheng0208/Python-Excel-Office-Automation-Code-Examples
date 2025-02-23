import pandas as pd

url = "https://fchart.github.io/ML/table.html"
tables = pd.read_html(url)  # 擷取 HTML 表格
df = tables[0]  # 取第一個表格
df.to_excel("table.xlsx", index=False)
print("HTML 表格已儲存為 table.xlsx")
