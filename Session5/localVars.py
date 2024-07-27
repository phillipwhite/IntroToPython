globalVar = 1

def myfunc():
    localVar = 2
    print(globalVar)
    #print(localVar)

myfunc()
print(globalVar)
# print(localVar)

for i in range(5):
    print(i)

print(i)
