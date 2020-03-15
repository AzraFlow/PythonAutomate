#! Python3
# Code to insert blank rows at a specified row in a Workbook sheet
import logging
# logging.disable(logging.CRITICAL)  # Uncomment to disable debug logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import sys, openpyxl

# Get the starting row integer, number of lines to insert integer, and the file to manipulate from the command line.
if len(sys.argv) != 4:
    print('Usage: python blankRowInserter.py [starting row] [number of rows to insert] [Excel file name to manipulate]')
    sys.exit()
startRow = int(sys.argv[1])
insertRows = int(sys.argv[2])
sourceFile = sys.argv[3]
logging.debug('startRow (%s)' %(startRow))
logging.debug('insertRows (%s)' %(insertRows))
logging.debug('sourceFile (%s)' %(sourceFile))

# Load Workbook object with name sourceFile
wb = openpyxl.load_workbook(sourceFile)
ws = wb.active

# Move cells beyond blank row to their new location.
for row in range(ws.max_row, startRow - 1, -1):  # loop trough the rows backwards to avoid cell overlap
    for column in range(1, ws.max_column + 1):
        logging.debug('row (%s)' %(row))
        oldCell = ws.cell(row=row, column=column)
        newCell = ws.cell(row=row + insertRows, column=column)
        newCell.value = oldCell.value

# Clear old values from blank rows.
for row in range(startRow, startRow + insertRows):
    for column in range(1, ws.max_column + 1):
        ws.cell(row=row, column=column).value = ''

# Define new filename and save the new file.
saveFile = str('new') + sourceFile
logging.debug('saveFile (%s)' %(saveFile))
wb.save(saveFile)
