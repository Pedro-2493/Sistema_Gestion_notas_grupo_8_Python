import requests

import pandas as pd



url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

# 1. Verificamos si la peticIón fue exitosa

if response.status_code == 200:

(datos))

Update



# 2. Si lo fue, extraemos el contenido JSON

datos = response.json()

print("¡Petición exitosal")

print("Tipo de datos recibidos:",

# Convertir los datos a DataFrame

print("Contenido:", datos)

df = pd.DataFrame([datos])

print("DataFrame:")



else:

print(f"Error al hacer la petición. Código de estado: {response.status_code}")