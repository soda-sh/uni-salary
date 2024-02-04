import openpyxl as excel
import openpyxl.utils as utils


class Excel:

    # searches for a value inside a column, then returns the first matching row
    def search(workbook, col, value):
        wb = excel.load_workbook(workbook)
        ws = wb.active

        colLetter = utils.get_column_letter(col)
        for item in ws[colLetter]:
            if item.value == value:
                row = item.row

        for row in ws.iter_rows(min_row=row, max_row=row, values_only=True):
            result = row

        return result


    def append(workbook, values):
        wb = excel.load_workbook(workbook)
        ws = wb.active

        ws.append(values)
        wb.save(workbook)
