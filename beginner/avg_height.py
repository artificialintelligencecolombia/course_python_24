# The program will calculate the average height from a number of students.
# The user will input the height of as many students he wants, then the script
# will perform the calculation
# avg = sum(heights) / number_of_students

print("\nAVERAGE HEIGHT CALCULATOR\n")

# Create the list that contains the data from students
heights_list = []

# User will input any number of students and the height of each one
while True:
    height_per_student = float(input("Write the height of the student: "))
    heights_list.append(height_per_student)
    print("Student with height: " + str(height_per_student) + " added.")
    add_student = input("\nDo you want to add another height to the list(yes/no)?: ")
    if add_student == "no":
        break

# Create the variable that contains the sum of the heights and the loop that
# will sum them.
total_height = 0
for height in heights_list:
    total_height += height

# Perform the calculation for the average height of the group
total_students = len(heights_list)
avg_height = total_height / total_students

# Print the results
print(f"The average height for the group of {total_students} students is: \n{avg_height}cm.")
print(f"Students list: \n {heights_list}")
