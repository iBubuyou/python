'''n = [3, -20, 10.00, 7, -32, -3.50]
sum = 0
for i in n :
    if i > 0 :
        sum = sum + i
        print(i)
print('sum = ',sum)'''



a = int(input("กรอกตัวเลขที่ 1 : "))
b = int(input("กรอกตัวเลขที่ 2 : "))
c = int(input("กรอกตัวเลขที่ 3 : "))
if (a > b and a < c) :
    print('ค่าที่อยู่ระหว่างกลาง ของ ',a,',',b,'และ',c,'คือ',a)
elif (b > a and b < c) :
    print('ค่าที่อยู่ระหว่างกลาง ของ ',a,',',b,'และ',c,'คือ',b)
else :
    print('ค่าที่อยู่ระหว่างกลาง ของ ',a,',',b,'และ',c,'คือ',c)