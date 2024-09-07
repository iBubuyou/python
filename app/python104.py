import pygal
import csv
def create_chart():
    balance = []
    with open("std_record.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for idx , row in enumerate(reader):
            if idx <= 4:
                balance.append(int(row[3]))   
    line = pygal.Line(height=400)
    line.title ="Line Chart"
    line.x_labels =("จันทร์","อังคาร","พุธ","พฤหัสบดี","ศุกร์")
    line.add("เงินคงเหลือ" , balance)
    line.render_in_browser()
create_chart()