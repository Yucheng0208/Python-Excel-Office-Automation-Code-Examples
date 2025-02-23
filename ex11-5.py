import requests

urls = [
    "https://fchart.github.io/Example.html",
    "https://fchart.github.io/books.html"
]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"成功擷取 {url} 的內容")
        print(response.text[:500])  # 只顯示前 500 個字
    else:
        print(f"無法擷取 {url}")
