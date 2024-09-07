import csv

with open('std_record.csv', mode = 'r', encoding = 'utf-8') as f:
    record = csv.reader (f, delimiter = ',')
    next(record, None)
    for row in record:
        a = row
        print(a[0])