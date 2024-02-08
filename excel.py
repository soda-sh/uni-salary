import openpyxl as excel
import openpyxl.utils as utils


class Excel:
    # searches for a value inside a list formatted excel file
    def listSearch(self, workbook, direction, headerName, value):
        wb = excel.load_workbook(workbook)
        ws = wb.active

        if direction == 'column':
            # finding the column to search inside for a match
            for cell in ws[1]:
                if cell.value == headerName:
                    colLetter = utils.get_column_letter(cell.column)

            # finding the matching row
            for cell in ws[colLetter]:
                if cell.value == value:
                    rowNumber = cell.row

            # result
            returnList = ws[rowNumber]

        elif direction == 'row':
            # finding the row to search inside for a match
            for cell in ws['A']:
                if cell.value == headerName:
                    rowNumber = cell.row

            # finding the matching column
            for cell in ws[rowNumber]:
                if cell.value == value:
                    colLetter = utils.get_column_letter(cell.column)

            # result
            returnList = ws[colLetter]

        else:
            # error
            return 'Specify the correct search direction'

        return returnList

    # searches for a value inside a table formatted excel file
    def tableSearch(self, workbook, colHeader, rowHeader):
        wb = excel.load_workbook(workbook)
        ws = wb.active

        # finding the coordinates of the cell
        for cell in ws[1]:
            if cell.value == colHeader:
                colLetter = utils.get_column_letter(cell.column)

        for cell in ws['A']:
            if cell.value == rowHeader:
                rowNumber = cell.row

        return ws[f'{colLetter}{rowNumber}']

    def append(self, workbook, values):
        wb = excel.load_workbook(workbook)
        ws = wb.active

        ws.append(values)
        wb.save(workbook)

    # creates an excel file and returns the name
    def createWorkbook(self, name):
        wb = excel.Workbook()
        wb.save(f"{name}.xlsx")
        return f"{name}.xlsx"
