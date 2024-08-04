# This script converts a user's name into the NATO phonetic alphabet.
# Each letter of the input name is replaced with its corresponding phonetic alphabet word.

# Import libraries
import pandas as pd

# Set the path of the alphabet's data
FILEPATH = './nato_phonetic_alphabet.csv'

# Convert the data to a dataframe
phonetic_df = pd.read_csv(FILEPATH)

# usr inputs the name
usr_input = 'Juana'

# Create a dictionary from the dataframe
# new_dict = {new_key: new_value for (index,value) in df.iterrows() if condition}
phonetic_dict = {row.letter:row.code for (index,row) in phonetic_df.iterrows()} 
# df.iterrows() iterates over the df rows -> each iteration returns the index and the row pairs.
# row.letter & row.code accesses the letter and code values of the current row
# for each row, it creates a key-value pair where key is 'row.letter' and value is 'row.code'.

# Create a new list with the phonetic codes based in the usr name's letters.
phonetic_name = [phonetic_dict[letter.upper()] for letter in usr_input if letter.upper() in phonetic_dict]
# phonetic_name = [...] -> constuct a list
# phonetic_dict[letter.upper()] -> looks for the letter in the dict and retrieves its respective phonetic code value.
# for each letter in the user name (string 'list')
# if letter.upper() in phonetic_dict -> checks if the current letter exists as key in the dictionary.

# Print the results
print(phonetic_name)