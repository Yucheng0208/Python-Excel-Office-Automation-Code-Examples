amounts = [900, 2500, 3300]  # 設定消費金額

for amount in amounts:
    if amount >= 1000:
        final_amount = amount * 0.8  # 8折
    else:
        final_amount = amount  # 不打折
    print(f"消費 {amount} 元，付款金額為: {final_amount:.2f} 元")