my_string = "Hello World!"
position = int(input("Which character do you want? enter an integer: "))
pos = 0
count = 0
for char in my_string:
    if pos == position:
        print("Character is at position", position, "is", char)
    pos += 1
    count += 1

print("length of string = ", count)
