# -*- coding: utf-8-*-

import xlsxwriter
import os
filelist = os.listdir('E:\PycharmProjects\write2excel\legal')
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
listno = len(filelist)
for filename in filelist:
    rdfile = open("E:\PycharmProjects\write2excel\legal\\" + filename, "r")
    software_list = rdfile.readlines()
    j = 0  #列数
    while j < listno:
        for software in software_list:
            rank = len(software_list)
            i = 1  #行数
            while i < rank + 1:
                worksheet.write(0, j, filename)
                worksheet.write(i, j, software )
                i = i + 1
    j = j + 1


workbook.close()




