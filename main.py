import csv
from prettytable import PrettyTable
# C://Users/Mark/Downloads/archive/russian_demography.csv
path_file = input('Enter file path: ')
column_number = int(input('Enter number of column: '))
with open(path_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    arr = []
    for row in reader:
        line = ' '.join(row)
        print(line)
        arr.append(row[column_number - 1])
arr[0] = 0
print('\nMaximum: ', arr)