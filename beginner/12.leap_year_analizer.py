# A leap year is the year that has 366 days.
# To determine whether a year is a leap year, the steps to follow are:

# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).

usr_year = int(input("Enter a year: "))

if usr_year % 4 == 0:
    if usr_year % 100 == 0:
        if usr_year % 400 == 0:
            print(f"{usr_year} is considered as a LEAP year.") 
        else:
            print(f"{usr_year} is not a leap year.")
    else:
        print(f"{usr_year} is considered as a LEAP year.")    
else:
    print(f"{usr_year} is not a leap year.")