# Create a script that converts the formart of a script, i. e. 'maD mAX' to 
# Title Case. Do it by using input & output functions

# 1. usr inputs a str
usr_str = input("Please, enter a name in random formating style (jUan dIeGO mOrENo):")

# 2. Create the function that changes the format
def title_formatter(name):
    name = name.title()
    return name

# 3. Store the function's output and store it in the var
user_titled = title_formatter(usr_str)

# 4. Print the result
print(f"Hello, {user_titled}, nice to meet you.")

