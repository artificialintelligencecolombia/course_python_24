# Pizza ordering script
# Based on user's order, print the bill of the order.
# Pizza sizes: Small= 15, Medium= 20, Large=25
# Additions: Pepperoni (Small= 2), Pepperoni (Medium or Large= 3)
# Additions: Extra cheese= 1 (For all sizes)
# Output: Thank you for choosing Python Pizza Deliveries! Your final bill is: $$$

print("Welcome to Python Pizza Delivery!\n\n")
pizza_size = input("What size pizza would you like (small, medium, or large)?: ").lower()
add_pepperoni = input("Would you like to add Pepperoni to your pizza? (yes/no): ").lower()
add_extra_cheese = input("Would you like to add extra cheese to your pizza? (yes/no): ").lower()

user_bill = 0

if pizza_size == "small":
    user_bill = 15
    if add_pepperoni == "yes":
        user_bill += 2
elif pizza_size == "medium":
    user_bill = 20
    if add_pepperoni == "yes":
        user_bill += 3
elif pizza_size == "large":
    user_bill = 25
    if add_pepperoni == "yes":
        user_bill += 3
else:
    print("Invalid values. Please try your order again.")

if add_extra_cheese == "yes":
    user_bill += 1

print(f"\nThank you for choosing Python Pizza Deliveries! Your final bill is: ${user_bill}")

