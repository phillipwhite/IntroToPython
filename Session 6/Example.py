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
