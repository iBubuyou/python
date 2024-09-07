import csv
with open('std_record.csv', mode='w', newline="") as f:
    w = csv.writer (f, delimiter=',')
    a = 1000
    b = 100
    c = 100
    d = a-b-c
    w.writerow([a,b,c,d])