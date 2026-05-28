import requests

import pandas as pd

url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

# 1. Verificamos si la peticIón fue exitosa

if response.status code == 200:

JSON

# 2. Si lo fue, extraemos el contenido

datos = response.Json()

print("¡Petición exitosal")

print("Tipo de datos recibidos:", type(datos))

print("Contenido:", datos)

# Convertir los datos a DataFrame

df = pd.DataFrame([datos])

print("DataFrame:")

else:

print (f"Error al hacer la petición. Código de estado: {response.status_code}")