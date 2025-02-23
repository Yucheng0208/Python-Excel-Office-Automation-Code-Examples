import openpyxl
from openpyxl.chart import LineChart, Reference

wb = openpyxl.Workbook()
ws = wb.active

# 輸入數據
data = [
    ["X", "Y1", "Y2"],
    [10, 20, 40],
    [20, 40, 10],
    [30, 10, 30]
]
for row in data:
    ws.append(row)

# 建立折線圖
chart = LineChart()
chart.title = "折線圖"
chart.x_axis.title = "X 軸"
chart.y_axis.title = "Y 軸"

x_values = Reference(ws, min_col=1, min_row=2, max_row=4)
y1_values = Reference(ws, min_col=2, min_row=1, max_row=4)
y2_values = Reference(ws, min_col=3, min_row=1, max_row=4)

series1 = Series(y1_values, x_values, title="第 1 條線")
series2 = Series(y2_values, x_values, title="第 2 條線")

chart.series.append(series1)
chart.series.append(series2)

ws.add_chart(chart, "E5")
wb.save("折線圖.xlsx")
