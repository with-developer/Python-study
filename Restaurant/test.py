import openpyxl
wb=openpyxl.load_workbook('/Users/junja/Desktop/python/Restaurant/example.xlsx') #파일명 혹은 패스+파일명 

test=wb.get_sheet_names()
print(test)