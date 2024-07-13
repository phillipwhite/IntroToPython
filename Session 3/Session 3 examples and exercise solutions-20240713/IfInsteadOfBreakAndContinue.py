userIsNotAuthenticated = True
while userIsNotAuthenticated:
    print('Who are you?')
    name = input()
    if name == 'Joe':
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input()
        if password == 'swordfish':
            userIsNotAuthenticated = False
print('Access granted.')
