import hashlib

# These lines can be removed completely
# to avoid showing the password in code
# PASSWORD = 'super_password123'
# PASSWORDhash = hashlib.md5(PASSWORD.encode('utf-8')).hexdigest()

PASSWORDhash = '63801b393517377de684a309e6fd79da'
password_entered = ''


while hashlib.md5(password_entered.encode('utf-8')).hexdigest() != PASSWORDhash:
    password_entered = input("Enter the password : ")
    if password_entered == PASSWORD:
        print("Access Granted!")
    else:
        print("Forbidden!")