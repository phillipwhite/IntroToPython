mylist = [1, 3, 6, 7, 9]
import random
random.shuffle(mylist)
print(mylist)

i = 0
while i in range(0,len(mylist), 1):
# while i < len(mylist):
    print(mylist[i])
    i += 1