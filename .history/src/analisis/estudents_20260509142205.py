import requests

import pandas as pd



url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

# 1. Verificamos si la peticIón fue exitosa

if response.status_code == 200:

    