entry = input("Enter an integer: ")
my_list = list([])

while entry != "q":
    my_list.append(int(entry))
    entry = input("Enter an integer: ")

print("Unsorted list:", my_list)
my_list.sort(reverse = True)
print("Sorted list:", my_list)

for element in my_list:
    print(element)

print(len(my_list))
print(max(my_list))
print(sum(my_list))