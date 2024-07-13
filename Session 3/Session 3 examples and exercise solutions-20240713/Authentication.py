PASSWORD = 'super_password123'
password_entered = ''
while password_entered != PASSWORD:
    password_entered = input("Enter the password: ")
    if password_entered == PASSWORD:
        print("Access Granted")
    else:
        print("Forbidden")