import random
# An example of a list comprehension to create list of 10 integers randomised between 1 and 100.

random_list = [random.choice(list(range(1, 100))) for i in range(10)]

def get_min_index(any_list):
    print("the min is", min(any_list))  # using the min builtin
    print("its index is", random_list.index(min(random_list))) # using the index method

print(random_list)
get_min_index(random_list)