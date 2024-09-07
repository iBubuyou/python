gender = input("เพศ : ")
height = int(input("ความสูง : "))
if gender == 'หญิง' and height < 100:
    print('ไม่เสียค่าผ่านทางประตู')
elif gender == 'หญิง' and height >= 100:
    print('เสียค่าผ่านประตู 25 บาท')
elif gender == 'ชาย' and height < 100:
    print('ไม่เสียค่าผ่านทางประตู')
elif gender == 'ชาย' and height >= 100:
    print('เสียค่าผ่านประตู 20 บาท')