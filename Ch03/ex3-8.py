H = float(input("請輸入身高值==>"))
W = float(input("請輸入體重值==>"))
BMI = W / ((H / 100) ** 2)
print(f"BMI 值是: {BMI:.6f}")