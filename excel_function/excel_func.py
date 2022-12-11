import random

from openpyxl import Workbook


def excel_random_numbers_table(title, col_numbrs, row_numbers):
    wb = Workbook()
    ws = wb[title]
    for i in range(1, col_numbrs):
        for j in range(1, row_numbers):
            # Заполняем лист случайными числами
            ws.cell(column=i, row=j, value=random.randint(1, 9))
    wb.save(title)
