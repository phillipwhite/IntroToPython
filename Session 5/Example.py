def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result
def maxabs(num1, num2):
    if abs(num1) > abs(num2):
        result = num1
    else:
        result = num2
    return result

print(max(2, 1))
print(max(2, 4))
print(maxabs(2, (1+01j) ))
print(maxabs(1, (1+01j) ))

def max_no_return(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    print(result)

print(max_no_return(20, 30))
print(type(max_no_return(20, 30)))

def my_separator():
    return("*" * 100)

for i in range(1, 6):
    print(my_separator())
    print(i)


def printGrade(score):
    # Print grade for the score
    if score >=90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    else:
        print('F')

printGrade(95)

def getGrade(score):
    # Print grade for the score
    if score >=90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'B'
    else:
        return 'F'

print(getGrade(85))

def nprintln(message, n):
    print("test")
    for i in range(0, n):
        print(message)

nprintln("hello ", 3)
nprintln(n=3, message="Hello ")



