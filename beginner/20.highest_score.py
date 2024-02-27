# User will input the scores of a class of students, the program will
# calculate and return the highest score

print("\nHIGHEST SCORE OF THE CLASS\n")

# Create the list that contains the data from students
scores_list = []
counter = 0

# User will input the score of each class student
while True:
    counter += 1
    student_score = int(input(f"Score of the student {counter}: "))
    scores_list.append(student_score)
    print("Scored added to the list.") 
    add_student = input("\nDo you want to add another score?(yes/no): ")
    if add_student == "no":
        break
    elif add_student != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
        
# Program will find the highest score
# enumerate() function returns pairs of index and value for each iteration
highest_rank = 0
highest_rank_index = -1
for index, student_rank in enumerate(scores_list):
    if student_rank > highest_rank:
        highest_rank = student_rank
        highest_rank_index = index


print(f"Highest rank in class was from Student {index} with score:\n{highest_rank}")
print(f"\nScores list:\n{scores_list}")