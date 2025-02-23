principal = float(input("請輸入本金: "))
years = 5
rate = 0.05

while years > 0:
    principal *= (1 + rate)
    years -= 1

print("5 年後的本利和:", round(principal, 2))