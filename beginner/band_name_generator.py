# The script will perform some questions, based on the user's input, it will
# return the band's name.

# Line breaks in string's console
# '\n' is used for line breaks in a string.
print("Hello world! \nHello world! \nHello world!\n")
print("Daniel\nMaldonado\nArias")

# input() function allows the user to prompt any kind of data
# We can write a function inside a function
usr_name = print("Hello " + input("What is your name?"))
alias = input(f"Nice to meet you, {usr_name[6:]}What is your alias?")
pet_name = input("What is your pet's name?")

# String concatenation
print("The bands name is: " + alias + " " + pet_name + " ," + usr_name + ".")

