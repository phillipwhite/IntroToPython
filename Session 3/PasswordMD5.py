import hashlib

PASSWORD = 'super_password123'
PASSWORDhash = hashlib.md5(PASSWORD.encode('utf-8')).hexdigest()
password_entered = ''

while hashlib.md5(password_entered.encode('utf-8')).hexdigest() != PASSWORDhash:
    password_entered = input("Enter the password : ")
    if password_entered == PASSWORD:
        print("Access Granted!")
    else:
        print("Forbidden!")