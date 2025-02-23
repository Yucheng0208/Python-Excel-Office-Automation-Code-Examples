weights = [3.5, 10, 25]  # 設定購物重量

for weight in weights:
    base_fee = 199  # 固定物流處理費
    if weight <= 5:
        shipping_fee = weight * 50  # 1~5 公斤，每公斤 50 元
    else:
        shipping_fee = 5 * 50 + (weight - 5) * 30  # 超過5公斤，每公斤 30 元

    total_fee = base_fee + shipping_fee  # 計算總運費
    print(f"購物重量: {weight} 公斤，總運費: {total_fee:.2f} 元")