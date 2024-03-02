# The program will calculate the sum of the even numbers from 1 to the use's
# input number. The total sum will be printed.

# User input the top number
print('\nSUM OF THE EVEN NUMBERS\n')
max_number = int(input('Enter the maximun number: '))

# Iterate through numbers from 0 to max_number and sum the even ones
even_sum = 0
for number in range(0,max_number+1,2): # It takes steps of 2 (starting from 0)
    even_sum += number

# Display the result
print(f"The sum of even numbers from 0 to {max_number} is:\n{even_sum}")