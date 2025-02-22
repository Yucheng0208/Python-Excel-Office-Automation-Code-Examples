# Q3
def calculate(a, b):
    if a > b:
        return a * b
    else:
        return a + b

def divide_or_neg_one(a, b):
    if b == 0:
        return -1
    return a / b

print(calculate(5, 3))  # 15
print(divide_or_neg_one(10, 2))  # 5.0
print(divide_or_neg_one(10, 0))  # -1

# Q4
def getMax(a, b, c):
    return max(a, b, c)

def getSum(a, b, c, d):
    return a + b + c + d

def getAverage(a, b, c, d):
    return (a + b + c + d) / 4

print(getMax(10, 20, 15))  # 20
print(getSum(10, 20, 30, 40))  # 100
print(getAverage(10, 20, 30, 40))  # 25.0

# Q5
def bill(minutes):
    if minutes <= 5 * 60:
        return minutes * 0.5
    else:
        return 5 * 60 * 0.5 + (minutes - 5 * 60) * 1

print(bill(300))  # 150.0
print(bill(400))  # 250.0

# Q6
def rate_exchange(twd, rate):
    return twd / rate

print(rate_exchange(1000, 30))  # 約 33.33 美元

# Q7
def bmi(height, weight):
    return weight / (height ** 2)

print(bmi(1.75, 70))  # 約 22.86

# Q8
def print_stars(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

print_stars(7)
