# -*- coding:utf-8 -*-
import xlrd

def rExCol(path):
    'Read the data from Excel file, and store the data into a list, the element of the list is single column'

    storelist = []    #Use this list to store all the data of the xls file.
    workbook = xlrd.open_workbook(path)
    SheetsList = workbook.sheets()
    sheetsn = len(SheetsList)

    for nsheet in range(sheetsn):
        sheet = workbook.sheet_by_index(nsheet)
        sheetrows = sheet.nrows
        sheetcols = sheet.ncols
        for nocols in range(sheetcols):
            col_data = sheet.col_values(nocols)
            storelist.append(col_data)
    return storelist

def rExRow(path):
    'Read the data from Excel files, and store the data into a list, the element of the list is single row'
    storelist = []
    workbook = xlrd.open_workbook(path)
    SheetsList = workbook.sheets()
    sheetsn = len(SheetsList)

    for nsheet in range(sheetsn):
        sheet = workbook.sheet_by_index(nsheet)
        sheetrows = sheet.nrows
        sheetcols = sheet.ncols
        for norows in range(sheetrows):
            row_data = sheet.row_values(norows)
            storelist.append(row_data)
    return storelist

def compare(book1, book2):
    'Compare excel file book1 using excel file book2.  The function will return the same element and the different element, two list in one tuple.'

    book1 = rExCol(book1)
    book2 = rExCol(book2)
    Book1Coln = len(book1)
    Book2Coln = len(book2)
    book1_list = []
    book2_list = []
    same = []
    diff = []

    for ColTmp in range(Book1Coln):
        RowNo = len(book1[ColTmp])
        for RowTmp in range(RowNo):
            book1_list.append(book1[ColTmp][RowTmp])
    for ColTmp in range(Book2Coln):
        RowNo = len(book2[ColTmp])
        for RowTmp in range(RowNo):
            book2_list.append(book2[ColTmp][RowTmp])
    for i in range(len(book1_list)):
        for j in range(len(book2_list)):
            if unicode(book1_list[i]) in unicode(book2_list[j]):
                same.append(book1_list[i])
            else:
                diff.append(book1_list[i])
    return same,diff
