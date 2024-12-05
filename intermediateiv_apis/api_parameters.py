import requests
from datetime import datetime
MY_LAT = 6.244203
MY_LONG = -75.581215
url = 'https://api.sunrise-sunset.org/json'

# Dictionary with the parameters of the API
parameters = { # the keys of the parameters my to match with the ones specified in the API.
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": 'America/Bogota',
    "formatted": 0
}

# Datetime
current_time = datetime.now()

# API
response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
current_hour = current_time.hour

print(f'Sunrise:\n{sunrise_hour}\n')
print(f'Sunset:\n{sunset_hour}\n')
print(f'Current hour: {current_hour}')