from PyPDF2 import PdfMerger

pdfs = ["file1.pdf", "file2.pdf", "file3.pdf", "file4.pdf", "file5.pdf", "file6.pdf"]
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("合併後.pdf")
merger.close()
print("已合併 6 個 PDF")
