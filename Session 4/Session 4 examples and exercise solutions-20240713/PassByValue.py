def m(number, list_of_numbers):
    number = 1001
    list_of_numbers[0] = 5555

def main():
    x = 1
    y = [1, 2, 3]
    m(x, y,)
    print("x is ", str(x))
    print("y[0] is", str(y[0]))
    print(y)

main()