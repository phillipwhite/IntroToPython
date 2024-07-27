# t1=()
# print(t1)
# print(type(t1))
#
# print([x for x in range(10)])
# print(tuple([x for x in range(10)]))
#
# my_list = [0, 1, 2]
# my_list[1] = 10
# print(my_list)
my_tuple = (0, 1, 2)
my_list = list(my_tuple)
my_list[0] = 10
my_tuple = tuple(my_list)
print(my_tuple)
print(max(my_tuple))
print(min(my_tuple))
print(len(my_tuple))
print(sum(my_tuple))
print(my_tuple[0:3])

t1 = ("g", "r", "b")
t2 = (7, 2, 3, 4)
t3 = t1 + t2
print(t1[-1])
for i in t1:
    print(i)

print("x" in t1)
l1 = list(t1).sort()
print(l1)