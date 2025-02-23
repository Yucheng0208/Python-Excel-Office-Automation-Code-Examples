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

bike = RacingBike("紅色", 8, 100, "競速車", 15000, 21, 50)
bike.display_racing_info()
