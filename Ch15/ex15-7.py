from docx import Document
from docx.shared import RGBColor, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

doc = Document("Python 開發環境.docx")

for para in doc.paragraphs:
    if "Python 開發環境" in para.text:
        run = para.runs[0]
        run.font.color.rgb = RGBColor(255, 0, 0)  # 紅色
        run.font.size = Pt(32)  # 字體大小
        para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 置中對齊

doc.save("Python 開發環境_修改版.docx")
print("已修改 Word 文件標題格式")
