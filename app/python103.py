import csv
def  display_summation():
  with open('std_record.csv', mode= 'r',) as f:
      record = csv.reader (f, delimiter=',')
      balance = []
      for row in record:
        balance.append(int(row[3]))
  print(balance)
  sum_data = sum(balance)
  print("เงินสะสม : ", sum_data, "บาท")