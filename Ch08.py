# Q4
file_path = input("請輸入檔案路徑: ")
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())

# Q5
file_path = input("請輸入檔案路徑: ")
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("總行數:", len(lines))

# Q6
file_path = input("請輸入程式碼檔案路徑: ")
output_path = "output.txt"

with open(file_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for idx, line in enumerate(infile, start=1):
        outfile.write(f"{idx:02d}: {line}")
print(f"已輸出至 {output_path}")

# Q7
class Box:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def volume(self):
        return self.width * self.height * self.length

    def area(self):
        return 2 * (self.width * self.height + self.width * self.length + self.height * self.length)

# 測試
box = Box(2, 3, 4)
print("體積:", box.volume())
print("表面積:", box.area())

# Q8
class Bicycle:
    def __init__(self, color, weight, wheelbase, model, price):
        self.color = color
        self.weight = weight
        self.wheelbase = wheelbase
        self.model = model
        self.price = price

    def display_info(self):
        print(f"顏色: {self.color}, 重量: {self.weight}kg, 輪距: {self.wheelbase}cm, 車型: {self.model}, 價格: {self.price}元")

class RacingBike(Bicycle):
    def __init__(self, color, weight, wheelbase, model, price, gears, top_speed):
        super().__init__(color, weight, wheelbase, model, price)
        self.gears = gears
        self.top_speed = top_speed

    def display_racing_info(self):
        self.display_info()
        print(f"變速段數: {self.gears}, 最高時速: {self.top_speed}km/h")

# 測試
bike = RacingBike("紅色", 8, 100, "競速車", 15000, 21, 50)
bike.display_racing_info()
