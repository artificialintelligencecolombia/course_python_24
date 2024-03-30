# Create script that 1.analize it a year (usr_year) is leap and 2.analizes 
# the month of that year (usr_month) and 3. returns if the year is leap and
# how many days the user's month has.

# 1. Ask for the year to the user
usr_year = int(input("Enter a year: "))
usr_month = int(input("Enter a month (1-12): "))

# 2. Create the function that analizes the year
def is_leap_year(year):
    """Hello, this is a docstring from
    the function. You can see it when calling the function."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else:
            return True    
    else:
        return False
    
# 3. Create the function that prints the number of days of the month
def days_in_month(month):
    twelve_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(usr_year) == True:
        twelve_months[1] = 29
    return twelve_months[month - 1]

number_of_days = days_in_month(usr_month)

print(number_of_days)     

