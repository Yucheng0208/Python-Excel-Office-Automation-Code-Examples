import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False

wb = excel.Workbooks.Open(r"ExcelVBA 爬蟲程式.xlsm")
excel.Application.Run("Module1.爬蟲執行")  # 假設 VBA 宏名稱為 "爬蟲執行"

wb.SaveAs(r"ExcelVBA_結果.xlsx")
wb.Close()
excel.Quit()

print("已結果儲存為 ExcelVBA_結果.xlsx")
