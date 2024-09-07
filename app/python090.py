def user_login(): 
    import csv
    with open('users.csv', mode= 'r',) as f:
        record = csv.reader (f, delimiter=',')
        next(record,None)
        users = []
        passwords = []
        for row in record:
            users.append(row[0])
            passwords.append(row[1])
    username = input("ชื่อผู้ใช้ระบบ: ")
    password = input("รหัสผ่าน :")
    if username in users and password in passwords:
        return True
    else:
        return False