PASSWORD = 'super_password123'
password_entered = ''
counter = 0

while password_entered != PASSWORD and counter < 3:
    password_entered = input("Enter the password : ")
    counter += 1
    if password_entered == PASSWORD:
        print("Access Granted!")
    else:
        print("Forbidden! That was attempt number", counter)

print("Forbidden after three failed attempts!")