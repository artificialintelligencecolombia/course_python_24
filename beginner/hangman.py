# HANGMAN GAME
#
# Flowchart:
# 1. Randomly choose a word from a list of words and assign it to a variable called chosen_word. 
# 2. Ask usr to guess a letter, assign the answer to a variable called guess. Make guess lowercase.
# 3. Check if letter of 'guess' is one of the letters in chosen_word.

# Import modules
import random

# Create the set of stages for the game
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

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

# Print the welcome message for the game
print("WELCOME TO HANGMAN GAME!\n") 

# check chosen word
print(chosen_word)    

# Generate as many blanks as the chosen_word
blank_str = ["_"] * len(chosen_word) 
print(blank_str)

# Create the list that will contain the user guessed letters
letters_list = []

# Define the lives of the user and end_of_game variable
end_of_game = False 
lives = 6

# User guesses a letter through the while loop 
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosen_word):
        if guess == letter:
#            print("Right")
            blank_str[index] = guess
    letters_list.append(guess)
#        else:
#            print("Wrong")
        
    # Define the conditions when the user enters a non existing letter in the word
    if guess not in chosen_word:
        print("Try again.")
        letters_list.append(guess)
        lives -=1
        print(lives)
        if lives == 0:
            print("You ran out of lives. GAME OVER.")
            end_of_game = True
    
    # Print the game score and stages
    print(stages[lives])
    print(blank_str)
    print(f"Used letters:{letters_list}")
    
    # Define the winning condition
    if "_" not in blank_str:
        print("YOU WON. End of the game.")
        end_of_game = True
