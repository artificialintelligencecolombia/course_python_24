# The program will ask you to hide a treasure in a 3 x3 grid
#   TREASURE MAP:
#   |   |   |   |
#   |   |   |   |
#   |   |   |   |
# By indexing a, b ,c as the columns and 0, 1, 2 as the rows, input the desired
# position (map[column][row]) for hiding the treasure.
# Print the already hidden treasure's map.



# Map
line_0 = [" "," "," "]
line_1 = [" "," "," "]
line_2 = [" "," "," "]
map = [line_0, line_1, line_2]
letters = ["a","b","c"]

# User enters the position
print("\n\nWELCOME TO 'HIDE THE TREASURE'\n")
print("  A    B    C")
print(f"0{line_0}\n1{line_1}\n2{line_2}")
position = input("\nEnter the position where the treasure will be hidden.\n(a0, b2, c1): ")

# Take the position values and convert them to indexes (ints)
position_letter = position[0].lower()
letter_index = letters.index(position_letter)
num_index = int(position[1])


# Store the "X" into the selected position in the map's nested list
map[num_index][letter_index] = "X"

# Print the treasure's map
print(f"\nLocation of the treasure: {position}\n")
print("  A    B    C")
print(f"0{line_0}\n1{line_1}\n2{line_2}")