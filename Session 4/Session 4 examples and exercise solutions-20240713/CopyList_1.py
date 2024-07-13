list1 = [1, 2, 3, 4, 5]
print("1. list1:", list1, " id: ", id(list1))
list2 = [x for x in list1] # Use comprehension to create new list object.
print("2. list2:", list2, " id: ", id(list2))
list3 = list1[:] # Slice/substring all elements to create new list object
print("3. list3:", list3, " id: ", id(list3))
list4 = list(list1) # Use constructor to create new list object.
print("4. list4:", list4, " id: ", id(list4))
import copy
list5 = copy.copy(list1) # Shallow copy creates new list object using references to the copied list.
print("5. list5:", list5, " id: ", id(list5))
list6 = copy.deepcopy(list1) # Deep copy creates new list object.
print("6. list6:", list6, " id: ", id(list6))
