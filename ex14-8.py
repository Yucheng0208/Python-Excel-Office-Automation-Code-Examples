import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock.csv")

plt.plot(df["日期"], df["收盤價"], marker="o", linestyle="-", label="股價")
plt.xlabel("日期")
plt.ylabel("收盤價")
plt.title("5 天股價折線圖")
plt.legend()
plt.grid(True)
plt.show()
