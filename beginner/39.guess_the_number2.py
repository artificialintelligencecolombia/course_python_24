import random

# Set global variables
EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

# Function to check user's guesses against target number
def check_guess(guess, answer, turns):
    """Checks the secret number against user's guess. Return the number of remaining opportunities."""
    if guess == answer:
        print(f"You got it, the correct answer is {guess}. YOU WON!")
    elif guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print("INVALID VALUE. Try again.")

# Function to set difficulty
def set_difficulty():
    # Set difficulty
    difficulty = [
        "Easy",
        "Hard"
    ]
    for level in difficulty:
        print("- ",level)
    
    level = input("Pick the level you want to play:").lower()
    if level == "easy":
        return EASY_LEVEL_LIVES 
    elif level == "hard":
        return HARD_LEVEL_LIVES
    else:
        print("Invalid input. Try again")
        set_difficulty()

# Game
def game():
    print("Welcome to Guess the number!!\n")

    # Target number
    secret_number = random.randint(1, 100)
    print(f"Secret number: {secret_number}")
    # Intro message
    print("I´m thinking in a number between 0 and 100.")

    # Set difficulty
    lives = set_difficulty()
    print(f"You have {lives} lives.\n")

    # Initialize the variable 
    usr_guess = 0

    # Iteractive loop
    while usr_guess != secret_number:
        print(f"You have {lives} remaining attempts.")
        
        # User guess
        usr_guess = int(input("Enter a number: "))
        
        # Ue the function for checking the user guess
        lives = check_guess(usr_guess, secret_number, lives)
        
        # Condition when lives goes to zero
        if lives == 0:
            print("You've ran out of lives. YOU LOOOSE(r). Lol.")
            return
        elif usr_guess != secret_number:
            print("Try again.\n")
        
game()