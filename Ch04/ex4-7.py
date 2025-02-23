height = float(input("請輸入您的身高 (cm): "))

if height < 120:
    print("門票：免費")
elif height <= 150:
    print("門票：半價")
else:
    print("門票：全票")