import requests
import json

url = "https://fchart.github.io/json/TaiwanRailway.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("TaiwanRailway.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("JSON 檔案已下載並儲存為 TaiwanRailway.json")
else:
    print("下載失敗")
