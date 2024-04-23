# Guess the number

import random

# 1. Welcome message
print("Welcome to guess the number game!\n")

# 2. Ask the level of the game
difficulty = [
    "Easy",
    "Hard"
]

# 3. Print the levels for the user to pick anyone
for level in difficulty:
    print("- ",level)
level = input("Pick the level you want to play:").lower()

# 4. Define the lives of the player
lives = 5
if level == "easy":
    lives = 10

# 5. Store the secret number in a variable. Define the token for winning the game
secret_number = random.randint(1, 100)
winning = False

while lives > 0 and winning == False:
    # 3. User enters the first guess.
    usr_input = int(input("Enter a number: "))
    
    # pc checks if usr_num = pc_num, if higher or lower.
    if usr_input == secret_number:
        print("You guessed the correct number. YOU WON!")
        winning = True
        break
    
    elif usr_input > secret_number:
        print("Too high, try again")
        lives -=1
    elif usr_input < secret_number:
        print("Too low, try again")
        lives -=1
    else:
        print("INVALID VALUE. Try again.")
    
    print(f"You have {lives} lives left. \n")

    if lives == 0:
        print("Saddly, you ran out of lives. Better luck in next time.")
        break





    
