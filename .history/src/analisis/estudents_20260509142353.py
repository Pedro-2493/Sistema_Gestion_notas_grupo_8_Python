import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)

# 1. Verificamos si la petición fue exitosa
if response.status_code == 200:
    # 2. Si lo fue, extraemos el contenido JSON
    datos = response.json()
    
    print("¡Petición exitosa!")
    print("Tipo de datos recibidos:", type(datos))
    print("Contenido:", datos)
    
    # Convertir los datos a DataFrame
    df = pd.DataFrame([datos])
    
    print("DataFrame:")
    print(df)

else:
    print(f"Error al hacer la petición. Código de estado: {response.status_code}")