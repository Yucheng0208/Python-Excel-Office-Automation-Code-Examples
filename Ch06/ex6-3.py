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