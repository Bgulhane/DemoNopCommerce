import openpyexcel


def getRowCount(file, sheetname):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook[sheetname]
    return sheet.max_row

def getCoulmnCount(file, sheetname):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook[sheetname]
    return sheet.max_column

def readData(file, sheetname, rownumber, column):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook[sheetname]
    return sheet.cell(row=rownumber, column=column).value


