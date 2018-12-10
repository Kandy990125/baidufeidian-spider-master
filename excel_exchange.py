# -*- coding=utf-8 -*-
import xlrd
from xlwt import Workbook
name_list = ["蔡徐坤", "白宇", "陈立农",
             "邓伦", "范丞丞", "华晨宇",
             "黄景瑜", "黄子韬", "林彦俊",
             "罗云熙", "王俊凯", "易烊千玺",
             "朱一龙", "朱正廷", "吴磊"]
def main():
    data_read = xlrd.open_workbook('1210-2.xls')
    table = data_read .sheets()[0]
    book = Workbook()
    sheet = book.add_sheet("sheet1")
    num = 0
    j = 1
    while j < table.ncols-2:
        i = 2
        name = str(table.cell(1, j).value).encode('utf-8')
        if name not in name_list:
            j = j + 1
            continue
        while i < table.nrows-2:
            time = str(table.cell(i, 0).value).split(' ')
            year = time[0]
            hour = time[1]
            sheet.write(num, 0, year)
            sheet.write(num, 1, hour)
            sheet.write(num, 2, name.decode('utf-8'))
            sheet.write(num, 3, table.cell(i, j).value)
            num = num + 1
            i = i + 1
        j = j + 1
    book.save('1210-final-30min.xls')
main()