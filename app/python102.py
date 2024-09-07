import csv 
import os
os.system('cls')
def display_data(): 
    with open("std_record.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        print()
        for row in reader:
            print(row[0],row[1],row[2],row[3],row[4])