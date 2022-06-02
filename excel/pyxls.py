import openpyxl
import random

wb = openpyxl.Workbook()

ws = wb.active

ws.title = 'data'

ws.append(['순번','제품명','가격','수량','합계'])

wb.save('./excel/test.xlsx')
