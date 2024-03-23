# 1. Creating a new dictionary
dictionary = {
    "red":"blood",
    "black": "ink",
    "blue": "ocean"
}

# 2. Calling an item by its key name.
print(dictionary["blue"], "\n\n")

# 3. Adding new (editing already existing) items to the dictionary.
dictionary["yellow"] = "sun"

# Empty dictionary
# Its often used as when we create empty lists or empty strings.
empty_dictionary = {}

# Delete all items from the dictionary
# ```
# dictionary = {}
# print(dictionary["yellow"]) # Error
# ```
# Loop through all items in the dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])