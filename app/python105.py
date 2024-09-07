import statistics
import csv 
def display_average():
    income = []
    balance = []
    with open("std_record.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            income.append(int(row[0]))
            balance.append(int(row[3]))
    avg_income = statistics.mean(income)
    avg_balance = statistics.mean(balance)
    print("ค่าเฉลี่ยของเงินฝาก",avg_income,"บาท")
    print("ค่าเฉลี่ยของเงินเหลือ",avg_balance,"บาท")
display_average()