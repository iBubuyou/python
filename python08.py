'''a = 15
b = 7
c = 9
if a > b:
    a = 1
    b = 2
    c = 3
print(a)
print(b)
print(c)'''

'''a = 15
b = 10
if a > b:
    max = a
else :
    max = b
print(max)'''

score = int(input ('Enter your score : '))
if score >= 80 :
    grade = 'A'
    msg = 'Very Good!'
elif score >= 70 :
    grade = 'B'
    msg = 'Good!'
elif score >= 60 :
    grade = 'C'
    msg = 'Okay!'
elif score >= 50 :
    grade = 'D'
    msg = 'Not Bad!'
else :
    grade = 'F'
    msg = 'Fail!'
print('Your score is',score , end = '')
print(' and you get',grade,'=',msg)