# Body Mass Index
# Measurement of body fat bvased in height and weight.
# BMI Categories: Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

# 1. Asks for required information and store it as strings.
usr_name = input("Hello, what's your name?: ")
usr_height = input(f"Nice to meet you, {usr_name}. Please, provide us your height in meters: ")
usr_weight = input("OK. Now, please provide your weight in kilograms: ")

print(f"\n\nFor confirmation, your name's {usr_name}, with a height of {usr_height} mts and weight of {usr_weight} kgs.")

bmi = round(float(usr_weight) / (float(usr_height)**2),2)

print(f"\nAccording with the data, your Body Mass Index's {bmi}: ")

if 0 < bmi < 18.5:
    print("You are underweight.")
elif 18.5 < bmi < 24.9:
    print("You are in normal weight.")
elif 25 < bmi < 29.9:
    print("You are overwight.")
else:
    print("You have obesity")