# The script will ask the user to input a random number. Then it will sum
# its digits and return the result.

# 1. User inputs number -> The input data type's a str
user_input = input("Write a random number: ")

# 2. Create the variable that store the sum of the digits
digits_sum = 0

# 3. Create the loop for interating through each digit of the user_number. For the
# sum we've to convert each digit(which is a str) to a int(). Then operates the loop's
# operation.
for digit in user_input:
    digits_sum += int(digit)
    
# sums it to the result poll
print("The sum of digits is: ", digits_sum)
# 4. Print the result 

print(3 * 3 + 3 / 3 - 3)