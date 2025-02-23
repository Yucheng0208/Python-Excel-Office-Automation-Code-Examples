df = pd.read_excel("台積電 2019 年 9 月股價.xlsx")
df.plot(kind="bar", x="日期", y="Volume", title="台積電成交量")
df.plot(kind="scatter", x="日期", y="Volume", title="台積電成交量散佈圖")
plt.show()
