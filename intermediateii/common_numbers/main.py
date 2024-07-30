# Create a list result which contains the numbers that are common in both files.

# set the filepath of the files
filepath1 = './numeric_list1.txt'
filepath2 = './numeric_list2.txt'

# Read the txt files in read mode
def read_number_from_file(filepath):
    with open(filepath, 'r') as file:
        numbers = file.readlines() # Read all lines into a list (including \n: newline characters)
        return [int(line.strip()) for line in numbers]

# Read the lists and convert them to lists of numbers
list1 = read_number_from_file(filepath1)
list2 = read_number_from_file(filepath2)

result = [item for item in list1 if item in list2] # Create a new list with items that are in both list1 and list2

# Print the result
print("Common numbers in both lists:")
print(result)
    
