# We can nest lists and dictionaries into dictionaries

# Nesting lists
travels = {
    "France": "Paris",
    "Canada": "Quebec",
    "Colombia": ["Bogota", "Medellin"]
    
}

# Nesting dictionaries 
countries_and_capitals = {
    {
        "country": "United States",
        "capital": "Washington, D.C.",
        "major_cities": ["New York", "Los Angeles", "Chicago"]
    },
    {    
        "country": "France",
        "capital": "Paris",
        "major_cities": ["Lyon", "Marseille", "Toulouse"]
    },
    {
        "country": "Japan",
        "capital": "Tokyo",
        "major_cities": ["Osaka", "Yokohama", "Nagoya"]
    }
}

# the primary difference between nesting dictionaries and lists involves how you 
# access their elements: Nested Dictionaries: You use keys to access elements.
# Nested Lists: You use integer indices to access elements. 