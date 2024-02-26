# Conditionals
# if condition:
#   do this
# else:
#   do that

height_standard = 120

usr_height = int(input("Please enter your height (in centimeters): "))

if usr_height >= height_standard:
    usr_age = int(input("Please enter your age: "))
    entrace_ticket = 0
    if usr_age >= 18:
        print("Entrance ticket's $40")
        entrace_ticket += 40
    else:
        print("Entrance ticket's $25")
        entrace_ticket += 25
        
    usr_photo = input("Do you want to get a photo (yes/no)?: ")
    if usr_photo == "yes":
        entrace_ticket += 5
        print(f"\nThe total bill, with photo included is ${entrace_ticket}.")
    else:
        print(f"\nThe total bill, NO photo is ${entrace_ticket}.")
            
    print("\nYou can pass. Enjoy :)!")
else:
    print(f"Your height is {usr_height} cms, you can't pass. Sorry :(.")