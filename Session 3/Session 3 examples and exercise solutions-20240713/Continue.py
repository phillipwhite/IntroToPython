sum = 0
number = 0
while number < 3:
    number += 1
    if number == 2:
        continue
    sum += number
    print('number = ', number, 'sum = ', sum)
print("The sum is ", sum)
