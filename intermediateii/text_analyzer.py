# Use dictionary comprehension to create a dict that takes each word in the given text and calculates the number of letters in each word.

sentence = 'Data breaches exposed over 4 billion records in the first half of 2019.'

# Convert the string to a list
list_of_words = list(sentence.split(' '))

# Create the dictionary by using dictionary comprehension
words_dict = {word:len(word) for word in list_of_words}
print(words_dict)
