# -*- coding:utf-8 -*-
import xlrd

def rExCol(path, storelist):
    'Read the data from Excel file, and store the data into a list, the element of the list is the data of single column'

    storelist = []
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

def rExRow(path, storelist):
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
