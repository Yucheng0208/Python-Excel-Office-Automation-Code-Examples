from PIL import Image, ImageDraw, ImageFont

# 開啟圖片並轉換為正方形
img = Image.open("input.jpg")
min_side = min(img.size)
img = img.resize((min_side, min_side))

# 設定浮水印文字
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 50)
text = "讀者姓名"
text_width, text_height = draw.textsize(text, font=font)

# 設定文字位置
position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
draw.text(position, text, fill="white", font=font)

# 存檔
img.save("output.jpg")
print("圖片已添加浮水印，存為 output.jpg")
