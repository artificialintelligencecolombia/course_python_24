# We can have global scope variables and local scope variables

# global scope
enemies = 1

def call_enemies():
    enemies = 2 # local scope
    print(f"Enemies from function: {enemies}")

call_enemies()
print(f"Enemies outside the function: {enemies}")

# constants are unmodifiedable values instances
PI = 3.1416 