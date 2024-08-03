# Employ dictionary comprehension to convert dictionary values from celcius to farenheit.

# Data
med_weather_data = {
    'vie_2/8': 15,
    'sab_3/8': 26,
    'dom_4/8': 26,
    'lun_5/8': 25,
    'mar_6/8': 24,
    'mie_7/8': 25,
    'jue_8/8': 25,
    'vie_9/8': 27,
    'sab_10/8': 28,
    'dom_11/8': 27
}

weather_farenheit = {day:(temperature * 9/5) + 32 for (day,temperature) in med_weather_data.items()} # .items() ensures you are iterating over both the keys and the values of the dictionary
print("Week's weather data (farenheit): ")
print(weather_farenheit)