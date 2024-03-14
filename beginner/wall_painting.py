# The goal is to calculate how many cans of paint are necessary to paint a wall.
# One can can paint 5 sqrd meters of wall
# Create a function where the user inputs the dimensions

print("PAINT CALCULATION")

wall_height = int(input("Enter the heiht of the wall: "))
wall_width = int(input("Enter the width of the wall: "))

def cans_calculation(height, width):
    area = height * width
    total_cans = area / 5
    print(f"Is it necessary to buy {total_cans} to paint a wall of {area} squared meters.")
    
cans_calculation(wall_height, wall_width)