# This program calculates the weeks left for a human based on their current age.
# The number of weeks in a year is: 52.143
# The calculation of the remaining time for a human is based on a 90-year life cycle.

# 1. Use 'datetime' module to work with dates and stores the current date into a var.
from datetime import date 
current_date = date.today()

# 2. Asks the user to input his/her birth date in a certain format (YYYY-MM-DD)
birth_date_usr_str = input("\nEnter your birth date (YYYY-MM-DD): ")

# 3. Parses the 'birth_date_usr_str' into a datetime.date object

try:
    birth_date_usr = date.fromisoformat(birth_date_usr_str)

except ValueError:
    print("Invalid date formate. Please use YYYY-MM-DD.")
    
# 4. Calculate age by subtracting birth date from current date

age = (current_date - birth_date_usr).days
weeks_left = ((90 * 365.25) - age) / 7

# 5. Print the results
print(f"\nYour current age is {round(age/365,2)} years.")
print(f"\nIf you'll live until 90 years old, you have approximately {weeks_left} weeks left.")
