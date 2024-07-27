from Session6_1.ListOfCountries import COUNTRIES
import random

countries = list(COUNTRIES.keys())
country_to_guess = random.choice(countries)
print(country_to_guess)

guess = input("Enter the capital of " + country_to_guess + "?")
if guess == COUNTRIES[country_to_guess]:
    print("Correct")
else:
    print("The correct capital is", COUNTRIES[country_to_guess])