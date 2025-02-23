product = 1  # 初始乘積設為 1
count = 0  # 計數器

while count < 4:
    num = int(input("請輸入數字: "))
    if num == 0:
        continue  # 跳過 0，不計入乘積
    product *= num
    count += 1  # 計算有效輸入次數

print("乘積結果:", product)
