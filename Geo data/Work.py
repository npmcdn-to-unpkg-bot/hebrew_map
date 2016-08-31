
import xlrd

workbook = xlrd.open_workbook('tempp.xlsx', on_demand = True)
value="מצרים";
#print (workbook.nsheets)
first_sheet = workbook.sheet_by_index(0);
for x in range(0,first_sheet.nrows):
    cell=first_sheet.cell(x,6);
    if (cell.value==value):
        res=(first_sheet.cell(x,8).value);

file = open('kml.txt', 'r')

for line in file:
    str=line.split();
    if (str[0]==res):
        print('('+str[2]+','+str[3]+')')






