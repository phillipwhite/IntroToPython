def reverse(list):
    result = []
    for element in list:
        result.insert(0, element)
        # Insert at position zero increases addresses of other elements in list by one.
    return result

list1 = [1, 2, 3, 4, 5, 6]
list2 = reverse(list1) # Call function reverse defined on line 1.
print(list2)

list3 = [1, 2, 3, 4, 5, 6]
list3.reverse() # Call reverse method for type list.
print(list3)

list4 = [1, 2, 3, 4, 5, 6]
list5 = sorted(list4, reverse=True)  # Uses Python sorted function.
print(list5)