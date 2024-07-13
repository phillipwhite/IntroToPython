data = []
num = input("Enter an integer ('q' to quit): ")
while num != 'q':
    data.append(int(num))
    num = input("Enter an integer ('q' to quit): ")
# data.sort(reverse=False)  # Uses list sort method.
data = sorted(data, reverse=True)  # Uses Python sorted function.
print("The values, sorted into ascending order are:")
for element in data:
    print(element)