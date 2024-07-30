# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing SEQUENCE:{string, tuple, list, range}.

# new_list = [new_item for item in list if condition]

list = [*range(1,11,1)]  # output: <class 'list'> -> with unpack operator '*' output: [...]

# Create a new list with the squared of the even numbers
new_list = [n**2 for n in list if n % 2 == 0]
print(new_list) # output: [4, 16, 36, 64, 100]

# Create a list from a list of names that only contain 4 letter names.
names = [
    "Alex",
    "Brianna",
    "Chris",
    "Danielle",
    "Eli",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Jessica",
    "Kyle",
    "Liam",
    "Monica",
    "Nathaniel",
    "Olivia"
]
short_names = [name for name in names if len(name) <= 4]
print(f'Short names: {short_names}') 

