import random
# An example of a list comprehension to create list of 10 integers randomised between 1 and 100.

random_list = [random.choice(list(range(1, 100))) for i in range(10)]

def get_min_index(any_list):
    min = 100
    index = 0
    for i in any_list:
        if i <= min:
            pass # Does not actually do anything. Can be used to indicate where code is to go.
            min = i
            min_index = index
        index += 1
    print("the min is", min)
    print("its index is", min_index)

print(random_list)
get_min_index(random_list)