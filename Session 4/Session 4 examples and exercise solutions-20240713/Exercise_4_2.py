def main():
    year = int(input("Enter a year: "))
    animals = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]
    print(year, " is the year of the ", animals[year % 12], sep = '') # Removes spaces when using separators.

main()