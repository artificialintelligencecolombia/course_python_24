# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing SEQUENCE:{string, tuple, list, range}.

# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,value) in dict.items() if condition}

import random

# Create a new dictionary form a list of students, with the name as the key and a random number as the value.
names = [
    "Alex",
    "Brianna",
    "Chris",
    "Danielle",
    "Eli",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Jessica",
    "Kyle",
    "Liam",
    "Monica",
    "Nathaniel",
    "Olivia"
]

student_scores = {student:random.randint(1,100) for student in names}
print("Student Scores: ")
print(student_scores)

# From the previous dictionary, pick the winner students and create a new dict with those students with score higher than 60
winner_students = {student:score for (student,score) in student_scores.items() if score > 60}
print('\nWinner students: ')
print(winner_students)

