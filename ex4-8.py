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