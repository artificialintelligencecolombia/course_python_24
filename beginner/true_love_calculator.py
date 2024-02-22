# Write a program that tests the compatibility between 2 people.
# 1. Take both names and check the number of times the letters of the owrd TRUE
# ocurrs in both names.
# 2. Take the names and check the number of times the letters of the owrd LOVE
# occurs.
# - Scores: less than 10 or greater than 90: Your score is #, you go togheter like
# cocke and mentos.
# - Scores: between 40 and 50: Your score is #, you're alright together.
# - Scores: another score: Your score is #.

girl_name = input("Enter the girl's name: ").lower()
boy_name = input("Enter the boy's name: ").lower()

true_sum = 0
love_sum = 0

for letter in girl_name + boy_name:
    if letter in ['t','r','u','e']:
        true_sum += 1
        
for letter in girl_name + boy_name:
    if letter in ['l','o','v','e']:
        love_sum += 1

score = str(true_sum) + str(love_sum)
score_int = int(score)

if score_int <= 10 or score_int >= 90:
    print(f"Your score is {score}, you go togheter like cocke and mentos.")
elif 40 <= score_int <= 50:
    print(f"Your score is {score}, you're alright together.")
else:
    print(f"Your score is {score}")
