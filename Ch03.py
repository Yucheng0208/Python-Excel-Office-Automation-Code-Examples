# Q3
num = int(input("請輸入數字: "))
a = "Tom"
var = 123
print(a, var, num)

# Q4
print(1 * 2 + 4)  # 6
print(7 / 5)      # 1.4
print(10 % 3 * 2 * (2 + 5))  # 14
print(1 + 2 ** 3)  # 9
print((1 + 2) * 3)  # 9
print(16 + 7 * 6 + 9)  # 67
print((13 - 6) / 7 + 8)  # 9.0
print(12 - 4 % 6 / 4)  # 11.0

# Q5
i = 1
i *= 5
i += 2
print("i =", i)  # 7

# Q6
x = y = 7
print("x =", x, "y =", y)
a, b = x, 10
print("a =", a, "b =", b)

# Q7
PI = 3.1415
r = float(input("請輸入半徑==>"))
circumference = 2 * PI * r
print(f"圓周長的值是: {circumference:.6f}")

# Q8
H = float(input("請輸入身高值==>"))
W = float(input("請輸入體重值==>"))
BMI = W / ((H / 100) ** 2)
print(f"BMI 值是: {BMI:.6f}")
