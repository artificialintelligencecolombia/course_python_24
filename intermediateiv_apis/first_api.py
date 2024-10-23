# We're making a request to the ISS location API to get THE LOCATION OF THE ISS in real time.

import requests # Import the requests library to handle HTTP requests 

# Define the URL for the ISS location API endpoint
url = 'http://api.open-notify.org/iss-now.json' #endpoint

# Make an HTTP GET request to the API to get the current ISS location
response = requests.get(url)
response.raise_for_status() # Raise an error if the HTTP response status code indicates a failure (not 2xx)status code -> will raise an HTTPError.
print(f"Response: {response}")
print(f"code: {response.status_code}")

# Hold the data of the API
data = response.json()
print(f"Global Data: {data}")

# We can access the values of the json file by calling the keys
longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']

iss_position = (longitude, latitude)
print(f"iss_position: {iss_position}")