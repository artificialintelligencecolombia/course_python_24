import datetime as dt

now = dt.datetime.now() # Prints the current datetime
# print(type(now)) datetime object

# Get current datetime and extract components
year = now.year
hour = now.timestamp()
print(year)
print(hour)

# Create custom datetime object for specific birth date
birth_date = dt.datetime(year=1999, month=5, day=27) # Creation of daytime obj
print(birth_date)



