# Q2
print("(1)", 2 + 3 == 5)  # True
print("(2)", 36 < 6 * 6)  # False
print("(3)", 8 + 1 >= 3 * 3)  # True
print("(4)", 2 + 1 == (3 + 9) / 4)  # True
print("(5)", 12 <= 2 + 3 * 2)  # False
print("(6)", 2 * 2 + 5 != (2 + 1) * 3)  # False
print("(7)", 5 == 5)  # True
print("(8)", 4 != 2)  # True
print("(9)", 10 >= 2 and 5 == 5)  # True

# Q3
x = 5
y = 6
z = 2
print("if x == 4:", x == 4)  # False
print("if y >= 5:", y >= 5)  # True
print("if x != y - z:", x != y - z)  # False
print("if z == 1:", z == 1)  # False
print("if y:", bool(y))  # True (y=6，非零數值為 True)

# Q4
if height > 20 and width >= 50:
    print("尺寸不合!")

# Q5
amounts = [900, 2500, 3300]  # 設定消費金額

for amount in amounts:
    if amount >= 1000:
        final_amount = amount * 0.8  # 8折
    else:
        final_amount = amount  # 不打折
    print(f"消費 {amount} 元，付款金額為: {final_amount:.2f} 元")

# Q6
weights = [3.5, 10, 25]  # 設定購物重量

for weight in weights:
    base_fee = 199  # 固定物流處理費
    if weight <= 5:
        shipping_fee = weight * 50  # 1~5 公斤，每公斤 50 元
    else:
        shipping_fee = 5 * 50 + (weight - 5) * 30  # 超過5公斤，每公斤 30 元

    total_fee = base_fee + shipping_fee  # 計算總運費
    print(f"購物重量: {weight} 公斤，總運費: {total_fee:.2f} 元")

# Q7
height = float(input("請輸入您的身高 (cm): "))

if height < 120:
    print("門票：免費")
elif height <= 150:
    print("門票：半價")
else:
    print("門票：全票")

# Q8
month = int(input("請輸入月份 (1~12): "))

if 3 <= month <= 5:
    print("這是春季")
elif 6 <= month <= 8:
    print("這是夏季")
elif 9 <= month <= 11:
    print("這是秋季")
elif month == 12 or 1 <= month <= 2:
    print("這是冬季")
else:
    print("輸入錯誤，請輸入 1~12 的數字")
