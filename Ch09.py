# Q6
import ch6_5_2  # 假設 `ch6-5-2.py` 與本程式在同一資料夾

a = int(input("請輸入第一個數字: "))
b = int(input("請輸入第二個數字: "))

print("最大值:", ch6_5_2.maxValue(a, b))

# Q7
import turtle

t = turtle.Turtle()

# 畫第一個長方形
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)

# 轉向以畫出第二個長方形
t.right(90)
t.forward(50)
t.left(90)

for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)

turtle.done()

# Q8
import win32com.client
import time

file_path = input("請輸入 PowerPoint 檔案路徑: ")

# 啟動 PowerPoint
ppt_app = win32com.client.Dispatch("PowerPoint.Application")
ppt_app.Visible = 1  # 設為可見
presentation = ppt_app.Presentations.Open(file_path)

# 開始播放簡報
presentation.SlideShowSettings.StartingSlide = 1
presentation.SlideShowSettings.EndingSlide = 3
presentation.SlideShowSettings.AdvanceMode = 1  # 手動播放
presentation.SlideShowSettings.ShowWithNarration = False
presentation.SlideShowSettings.ShowWithAnimation = True
presentation.SlideShowSettings.LoopUntilStopped = False
presentation.SlideShowSettings.RangeType = 1  # 設定範圍

# 開始播放
slideshow = presentation.SlideShowWindow
if slideshow is None:
    presentation.SlideShowSettings.Run()

# 自動間隔 2 秒播放前 3 頁
for _ in range(3):
    time.sleep(2)
    ppt_app.SendKeys("{RIGHT}")  # 模擬右鍵換頁

# 關閉簡報
time.sleep(2)
presentation.Close()
ppt_app.Quit()
