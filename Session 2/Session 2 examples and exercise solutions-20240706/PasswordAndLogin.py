PASSWORD = 'super_password123'
LOGIN = 'superadmin'
login_entered = input("Enter the login: ")
password_entered = input("Enter the password: ")
if password_entered == PASSWORD and login_entered == LOGIN:
    print("Access Granted")
else:
    print("Forbidden")


