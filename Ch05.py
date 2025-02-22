# Q3
total = 0
for i in range(40, 68):
    if i % 2 != 0:
        print(i, end=" ")
        total += i
print("\n總和:", total)

# Q4
for i in range(1, 21):
    print(i, i**2)

# Q5
length = float(input("請輸入繩索長度: "))
count = 0

while length >= 20:
    length /= 2
    count += 1

print("需要對折", count, "次")

# Q6
principal = float(input("請輸入本金: "))
years = 5
rate = 0.05

while years > 0:
    principal *= (1 + rate)
    years -= 1

print("5 年後的本利和:", round(principal, 2))

# Q7
for i in range(1, 6):
    print(str(i) * i)

# Q8
product = 1  # 初始乘積設為 1
count = 0  # 計數器

while count < 4:
    num = int(input("請輸入數字: "))
    if num == 0:
        continue  # 跳過 0，不計入乘積
    product *= num
    count += 1  # 計算有效輸入次數

print("乘積結果:", product)
