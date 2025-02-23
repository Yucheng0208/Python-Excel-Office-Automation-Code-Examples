import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
ws = wb.active

# 新增數據
data = [
    ["類別", "數量"],
    ["A", 30],
    ["B", 50],
    ["C", 40]
]
for row in data:
    ws.append(row)

# 建立長條圖
chart = BarChart()
chart.title = "銷售數據"
chart.x_axis.title = "類別"
chart.y_axis.title = "數量"

data_ref = Reference(ws, min_col=2, min_row=1, max_row=4)
categories_ref = Reference(ws, min_col=1, min_row=2, max_row=4)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(categories_ref)

ws.add_chart(chart, "E5")  # 設定圖表位置
wb.save("chart.xlsx")
print("圖表已儲存於 chart.xlsx")
