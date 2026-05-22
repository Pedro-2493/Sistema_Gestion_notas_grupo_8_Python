import requests

import pandas as pd

09052026

url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

# 1. Verificamos si la peticIón fue exitosa

if response.status_code == 200:

type(datos))

Update

D

10

11

12

# 2. Si lo fue, extraemos el contenido JSON

datos = response.json()

print("¡Petición exitosal")

print("Tipo de datos recibidos:",

# Convertir los datos a DataFrame

print("Contenido:", datos)

df = pd.DataFrame([datos])

print("DataFrame:")

14

15

16

17

18

else:

print(f"Error al hacer la petición. Código de estado: {response.status_code}")