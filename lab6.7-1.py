price = int(input('ราคาสินค้า : '))
discount = price*10/100
if discount >= 500:
    print("คูปองที่แลกได้ ราคา 500 บาท")
elif discount >= 100:
    print("คูปองที่แลกได้ ราคา 100 บาท")
elif discount >= 50:
    print("คูปองที่แลกได้ ราคา 50 บาท")
else :
    print('ไม่ได้รับคูปอง')