import csv
with open('std_record.csv', mode='a',newline="") as f:
    w = csv.writer (f, delimiter=',')
    a = 641
    b = 25
    c = 180
    d = a-b-c
    w.writerow([a,b,c,d])