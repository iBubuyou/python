import csv
import datetime

def create_data():
    with open('std_record.csv', mode='a') as f:
       w = csv.writer (f, delimiter=',')  
       a = int(input("รายรับวันนี้ : "))
       b=  int(input("ค่าขนม : "))
       c = int(input("ค่าอาหาร : "))
       d = a-b-c
       e = datetime.date.today()
       w.writerow([a,b,c,d,e]) 