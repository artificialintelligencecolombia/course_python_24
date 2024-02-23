# random module is a must for generating random numbers
import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random() # it generates a random number between 0 and 1
print(random_float)

# 1. Create a list with the departments of Colombia
colombia_departments = [
    "Amazonas",
    "Antioquia",
    "Arauca",
    "Atlántico",
    "Bogotá, D.C.",
    "Bolívar",
    "Boyacá",
    "Caldas",
    "Caquetá",
    "Casanare",
    "Cauca",
    "Cesar",
    "Chocó",
    "Córdoba",
    "Cundinamarca",
    "Guainía",
    "Guaviare",
    "Huila",
    "La Guajira",
    "Magdalena",
    "Meta",
    "Nariño",
    "Norte de Santander",
    "Putumayo",
    "Quindío",
    "Risaralda",
    "San Andrés y Providencia",
    "Santander",
    "Sucre",
    "Tolima",
    "Valle del Cauca",
    "Vaupés",
    "Vichada"
]

print(f"Colombia contains {len(colombia_departments)} departments.\n")

# 2. Define the random number generator.
random_number = random.randint(0, len(colombia_departments))

print(f"The department chosen randomly is:  {colombia_departments[random_number]}.")

# List functions

colombia_departments.append("Maldonadolandia")
print(colombia_departments[-1])
