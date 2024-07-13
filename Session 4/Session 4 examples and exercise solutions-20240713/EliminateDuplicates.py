def main():
    s = input("Enter numbers: ") # Read numbers as a string from the console
    items = s.split() # Extracts items from the string
    numbers = [int(x) for x in items] # Convert items to list called numbers
    print("The distinct numbers are:", eliminateDuplicates(numbers))

def eliminateDuplicates(list):
    result = [] 
    for element in list:
        if not (element in result):
            result.append(element)
    return result

main()