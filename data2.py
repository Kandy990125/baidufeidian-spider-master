# -*- coding=utf-8 -*-
import xlrd
from xlrd import xldate_as_tuple
import datetime
name_list = ["蔡徐坤", "白敬亭", "白宇", "陈坤", "陈立农", "陈伟霆", "邓伦", "范丞丞", "胡一天",
             "华晨宇", "黄景瑜", "黄明昊", "黄子韬", "李易峰", "林彦俊", "刘昊然", "罗云熙", "马天宇", "聂远",
             "王鹤棣", "王俊凯", "王凯", "王一博", "王源", "小鬼", "许凯", "许魏洲", "杨洋", "易烊千玺", "张杰",
             "张艺兴", "钟汉良", "朱一龙", "朱正廷", "胡歌", "韩东君", "侯明昊", "卜凡", "陈学冬", "毛不易", "王嘉尔",
             "肖战", "朱星杰", "黄轩", "雷佳音", "尤长靖", "王子异", "彭昱畅", "吴磊", "吴亦凡"]

def read():
    data = xlrd.open_workbook('1210.xlsx')
    table = data.sheets()[0]
    list = []
    i = 0
    while i < table.nrows:
        j = 0
        while j < 50:
            item = []
            result = xldate_as_tuple(table.cell(i, 0).value, 0)
            s1 = ""
            m = 0
            for time_item in result:
                if m == 0:
                    m = m + 1
                    continue
                time_item = str(time_item)
                if len(time_item) == 0:
                    time_item = "00"
                if len(time_item) == 1:
                    time_item = "0"+str(time_item)
                if m < 2:
                    s1 = s1 + time_item + "-"
                if m == 2 or m == len(result)-2:
                    s1 = s1 + time_item + " "
                if m > 2:
                    s1 = s1 + time_item + ":"
                m = m + 1
            s1 = s1[:-6]
            item.append(s1)
            s = filter(str.isdigit, str(table.cell(i, 1).value.encode('utf-8')))
            if s != "":
                item.append(s)
                item.append(table.cell(i, 2).value)
            else:
                item.append(table.cell(i, 2).value)
                item.append(table.cell(i, 3).value)
            if (s1[9] == '0' and s1[10] == '0') or (s1[9] == '3' and s1[10] == '0'):
                list.append(item)
            j = j + 1
            i = i + 1
    return list
def write(list):
    from xlwt import Workbook
    book = Workbook()
    sheet = book.add_sheet("sheet1")
    sheet.write(0, 0, "time")
    i = 0
    for item in list:
        # print item
        sheet.write(0, i+1, int(item[1]))
        if i >= 50:
            break
        i = i + 1
    sheet.write(1, 0, "time")
    i = 1
    for name_item in name_list:
        sheet.write(1, i, name_item.decode('utf-8'))
        i = i + 1
    i = 0
    row = 2
    while i < len(list):
        j = 0
        time = list[i][0]
        sheet.write(row, 0, time)
        while j < 50:
            num = list[i][1]
            vote = list[i][2]
            sheet.write(row, j+1, vote)
            j = j + 1
            i = i + 1
        row = row + 1
    book.save('1210-2.xls')
list = read()
write(list)