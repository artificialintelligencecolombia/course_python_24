# HANGMAN GAME
#
# Flowchart:
# 1. Randomly choose a word from a list of words and assign it to a variable called chosen_word. 
# 2. Ask usr to guess a letter, assign the answer to a variable called guess. Make guess lowercase.
# 3. Check if letter of 'guess' is one of the letters in chosen_word.

# Import modules
import random

# Create the list which contains the words
words_list = [
    "python",
    "hangman",
    "programming",
    "developer",
    "algorithm",
    "database",
    "interface",
    "framework",
    "repository",
    "authentication",
    "encryption",
    "iteration",
    "javascript",
    "structure",
    "iteration",
    "authentication",
    "validation",
    "repository",
    "framework",
    "developer"
]

# Program picks the word
chosen_word = random.choice(words_list)

# check chosen word
print(chosen_word)    

# Generate as many blanks as the chosen_wprd
blank_str = ["_"] * len(chosen_word) 
print(blank_str)

# Define the lives of the user and end_of_game variable
end_of_game = False 
lives = 6

# User guesses a letter through the loop
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosen_word):
        if guess == letter:
#            print("Right")
            blank_str[index] = guess
#        else:
#            print("Wrong")
    print(blank_str)
    
    if guess not in chosen_word:
        print("Try again.")
        lives -=1
        print(lives)
        if lives == 0:
            print("You ran out of lives. GAME OVER.")
            end_of_game = True
    
    if "_" not in blank_str:
        print("YOU WON. End of the game.")
        end_of_game = True

    
    