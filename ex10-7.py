from PIL import Image, ImageDraw, ImageFont

# 讀取文字檔案
with open("images_list.txt", "r") as f:
    images = f.read().splitlines()

# 浮水印設定
watermark = Image.open("watermark.png")
for image_file in images:
    img = Image.open(image_file)
    img.paste(watermark, ((img.width - watermark.width) // 2, (img.height - watermark.height) // 2), watermark)
    img.save(f"watermarked_{image_file}")
