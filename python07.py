"""a = 10/2
b = 10//2
c = 10%2
print(a, b, c)"""

birthday = "22/06/2545"
year = birthday[6:]
print(year)
str2int = int(year)
age = 2565 - str2int
print("คุณมีอายุ",age, "ปี")

a = int(input("จำนวนคน : "))
b = int(input("ราคาต่อหัว : "))
print(a,b)
d = a % 4 * 200
print(d)
e = a // 4
f = (4-1) * 200 * e + d
print(e)
print("total : ",f)