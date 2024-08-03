# This script converts a user's name into the NATO phonetic alphabet.
# Each letter of the input name is replaced with its corresponding phonetic alphabet word.

# Import libraries
import pandas as pd

# Set the path of the alphabet's data
FILEPATH = './nato_phonetic_alphabet.csv'

# Convert the data to a dataframe
phonetic_df = pd.read_csv(FILEPATH)

# usr inputs the name
usr_input = 'Daniel'

# new_dict = {new_key: new_value for (index,value) in df.iterrows() if condition}
usr_phonetic = {index:value for (index,value) in phonetic_df.iterrows()}

print(usr_phonetic)