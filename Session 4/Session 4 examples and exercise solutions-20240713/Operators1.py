list1 = [2, 3]
list2 = [1, 9]
list3 = list1 + list2
print(list3)
list3 = 2 * list1
print(list3)
list4 = list3[2:4] # Slice, or substring, from element with address two until element with address four minus one.
                   # So if list3 is [2, 3, 2, 3] then element with address two = 2, and address four minus one = 3.
print(list4)
# list5 = [1, 2, 3, 4, 5]
# print(list5[2:4])