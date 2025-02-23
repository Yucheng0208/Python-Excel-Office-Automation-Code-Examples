import requests

stock_symbol = "2330.TW"  # 台積電
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock_symbol}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("股票資料:", data)
else:
    print("無法獲取股票資訊")
