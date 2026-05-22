import requests
import pandas as pd

# The endpoint you want to fetch data from
url = "https://prueba-con-render.onrender.com/api/students"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (Status Code 200)
if response.status_code == 200:
    # Parse the response as JSON (converts it to a Python dictionary)
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")


df = pd.