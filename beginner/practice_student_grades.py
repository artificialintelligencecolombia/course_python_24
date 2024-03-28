# Create a program that interprets the scores from a dictionary of students and 
# their results and creates a new dictionary called 'student_grades' where
# each student has his grade.
# Grades:  91-100: Outstanding, 81-90: Exceeds Expectations, 71-80: Acceptable
# 70-Lower: Fail
# Expected output: {'student':'Acceptable', ... }

student_scores ={
    "Harry": 81,
    "Ron":78,
    "Hermione":99,
    "Draco": 74,
    "Neville": 62
}

# 1.Create an empty dictionary called 'student_grades'
student_grades = {}

# 2. Create a loop that iterates over student_scores
for student in student_scores:
    if student_scores[student] > 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 71:
        student_grades[student] = "Acepptable"
    else:
        student_grades[student] = "FAIL"    
# Print the results
print(student_grades)        
        
