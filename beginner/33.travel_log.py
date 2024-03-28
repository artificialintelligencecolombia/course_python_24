# Create a function that adds countries visited into a dictionary called 
# 'travel_log'

# 1. Create the empty 'travel_log' list.
travel_log = []

# Define the user inputs
country = input("Add the country you've visited: ")
number_visits = int(input("How many times did you visit it: "))
visited_cities = input("What cities did you visit? (e.g: Medellin, Bogota, Cali): ")

# Splitting and cleaning the cities
list_of_cities = [city.strip() for city in visited_cities.split(',')]
# 1. visited_cities.split(',') creates a list of cities
# 2. for city in list_of_cities iterates over the cities elements of the list
# 3. city.strip() takes each element and deletes its initial and final spaces

# Define the function for adding countries
def add_new_country(name, visits, cities):
    # Create a empty dictionary for new country
    new_country = {}
    new_country['name'] = name
    new_country['visits'] = visits 
    new_country['cities'] = cities
    travel_log.append(new_country)

    
add_new_country(country, number_visits, list_of_cities)
print(f"I've been in {travel_log[0]['name']} {travel_log[0]['visits']} times.")