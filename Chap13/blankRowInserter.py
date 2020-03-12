#! Python3
# Code to insert blank rows at a specified row in a Workbook sheet
import logging
# logging.disable(logging.CRITICAL)  # Uncomment to disable debug logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import sys, openpyxl

# Get the starting row integer, number of lines to insert integer, and the file to manipulate from the command line.
if len(sys.argv) != 4:
    print('Usage: python blankRowInserter.py [starting row] [number or rows to insert] [Excel file name to manipulate]')
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

rowData = ws.rows
logging.debug('rowData (%s)' %(rowData))
# Write the rows up to the startRow for inserted rows
for rowNum in range(1, startRow + 1):
    print(rowData(rowNum))

# Write the rows after the inserted rows
# for rowNum in range(startRow, sheet.max_row + 1):




saveFile = str('new') + sourceFile
logging.debug('saveFile (%s)' %(saveFile))
wb.save(saveFile)
