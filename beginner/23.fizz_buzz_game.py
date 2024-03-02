# The program will take 2 numbers chosen by user. We're going to take a 
# sample of 100 numbers, starting from 1. If a list's number is divisible
# by number A, the program prints 'Fizz'. If a list's number is divisible by
# number B, the program prints 'Buzz'. If the number is divisible by both A and B,
# prints 'FizzBuzz'. Print the whole list of numbers of the list.

# User inputs both numbers
number_a = int(input("Enter the 'Fizz' number: "))
number_b = int(input("\nEnter the 'Buzz' number: "))

for number in range(1,101):
    if number % number_a == 0 and number % number_b == 0:
        print('FizzBuzz')
    elif number % number_a == 0:
        print('Fizz')
    elif number % number_b == 0:
        print('Buzz')
    else:
        print(number)