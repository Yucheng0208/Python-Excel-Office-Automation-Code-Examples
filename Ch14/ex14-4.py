from openpyxl.chart import ScatterChart

chart = ScatterChart()
chart.title = "散佈圖"
chart.x_axis.title = "X 軸"
chart.y_axis.title = "Y 軸"

x_values = Reference(ws, min_col=1, min_row=2, max_row=4)
y_values = Reference(ws, min_col=2, min_row=2, max_row=4)
series = Series(y_values, x_values, title="資料點")
chart.series.append(series)

ws.add_chart(chart, "E10")
wb.save("scatter_chart.xlsx")
