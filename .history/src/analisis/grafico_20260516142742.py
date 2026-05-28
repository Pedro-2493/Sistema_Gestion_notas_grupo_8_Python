import matplotlib.pyplot as plt
import os
import pandas as pd

ruta_entrada = os.path.join(".","data","raw","estudiantes.csv")
df = pd.read_csv(ruta_entrada)

# 1. Preparar el lienzo (Ancho, Alto en pulgadas)
plt.figure(figsize=(10, 6))

# 2. Pintar el gráfico (usando la integración directa de Pandas)
df.plot(kind='bar', x='nombre', y='email', color='blue')
# 3. Personalización y Contexto (Metadata)
plt.title("Título Claro y de Negocio", fontsize=14)
plt.xlabel("Etiqueta del Eje X")
plt.ylabel("Etiqueta del Eje Y")
plt.xticks(rotation=45) # Rotar textos para que no colisionen

# 4. Renderizar (Mostrar a pantalla)
plt.show()
