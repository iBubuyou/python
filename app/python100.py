import os
import time
from python090 import user_login
from python101 import create_data
from python102 import display_data
from python103 import display_summation
from python104 import create_chart
from python105 import display_average

os.system('cls')

def show_menu(): 
    print("==== โปรแกรมบันทึกค่าใช้จ่ายประจำวัน ===== ")
    print("1. บันทึกรายการลงแฟ้มข้อมูล ")
    print("2. แสดงรายการทั้งหมดจากแฟ้มข้อมูล")
    print("3. แสดงผลรวมยอดเงินคงเหลือ")
    print("4. แสดงแผนภูมิรายการยอดเงินคงเหลือ")
    print("5. แสดงค่าเฉลี่ยค่าใช้จ่าย ")
    selected_menu = int(input('กรุณาเลือกรายการ[1-5] : '))
    if selected_menu == 1:  
        create_data()  
    elif selected_menu == 2:
        display_data()
    elif selected_menu == 3:
        display_summation()
    elif selected_menu == 4:
        create_chart()
    elif selected_menu == 5:
        display_average()
    else :
        print("กรอกข้อมูลผิดพลาด")

print("program loading...")
time.sleep(3)

user_account = user_login()
if user_account == True:
   show_menu()
elif user_account == False:
   print("คุณกรอกข้อมูลผิดพลาด")