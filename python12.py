import os
print("===== โปรแกรมบันทึกค่าใช้จ่ายประจำวัน =====")
print("1. บันทึกรายการลงแฟ้มข้อมูล ")
print("2. แสดงรายการทั้งหมดจากแฟ้มข้อมูล ")
print("3. แสดงผลรวมของเงินเหลือในแต่ละวัน ")
print("4. แสดงแผนภูมิ ")
selected_menu = int(input('กรุณาเลือกรายการ [1-4] : '))
if selected_menu == 1:
    pass
elif selected_menu == 2:
    pass
elif selected_menu == 3:
    pass
elif selected_menu == 4:
    import pygal
    import csv
    lst = [] #เก็บยอดเงินคงเหลือไว้ที่เดียวกันหรือแถวเดียวกัน
    lst_i = []
    with open("std_record.csv", mode= 'r') as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            balance = int(row[3])
            income = int(row[0])
            lst.append(balance)
            lst_i.append(income)
        print(lst)
    line = pygal.Line(height=400,inner_radius=.5)
    line.title = "รายงานยอดเงินคงเหลือ/รายรับในแต่ละวัน"
    line.x_labels = ('จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์')
    line.add('ยอดเงินคงเหลือ', lst)
    line.add('รายรับ', lst_i)
    line.render_in_browser()
else :
    print('คุณเลือกรายการผิด')
os.system('cls')