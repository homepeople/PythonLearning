#coding=utf-8
import xlwings as xw
wb = xw.Book(r'C:\Users\Fred\Desktop\test.xlsx')
wb.sheets[0].name="比较表"
sht=wb.sheets["比较表"]
sht.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
sht.range('A3').value ="Hello World"
rng=wb.sheets[0].range('A1:D5')
# rng=rng[:,3:]
# print(rng)
rng=rng[1:3,:]
print(rng)

#OPEN WORKBOOK
######################################
#open a new workbook
# wb = xw.Book()
#open a workbook file
# wb =xw.Book(r'C:\Users\Fred\Desktop\上门服务表.xlsm')
# open a workbook from a full path 
# FileName = "C:\\python\\to\\file.xlsx"
# FileName = r"C:\python\to\file.xlsx"
# 注意 windows 字符 "\" 逃逸的问题
# wb = xw.Book(FileName)
######################################

#OPEN SHEET
######################################
# sheet=wb.sheets[0]

