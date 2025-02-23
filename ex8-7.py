class Box:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def volume(self):
        return self.width * self.height * self.length

    def area(self):
        return 2 * (self.width * self.height + self.width * self.length + self.height * self.length)

box = Box(2, 3, 4)
print("體積:", box.volume())
print("表面積:", box.area())