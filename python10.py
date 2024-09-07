import csv
with open('std_record.csv', mode='a',newline="") as f:
    fieldnames = ['รับเข้า','ค่าขนม',"ค่าข้าว","เงินคงเหลือ"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    w = csv.writer (f, delimiter=',')
    a = 1000
    b = 100
    c = 100
    d = a-b-c
    w.writerow([a,b,c,d])