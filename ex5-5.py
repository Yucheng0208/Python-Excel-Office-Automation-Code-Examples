length = float(input("請輸入繩索長度: "))
count = 0

while length >= 20:
    length /= 2
    count += 1

print("需要對折", count, "次")