year = input("Enter a year : ")
year = int(year)
leap_year = False # boolean value saying if
                  # the year is a leap_year or not
if year % 400 == 0:
    leap_year = True
elif year % 4 == 0:
	if year % 100 != 0:
         leap_year = True
else:
    leap_year = False

if leap_year:
    print("The year entered is a leap year.")
else:
    print("The year entered is not a leap year.")
