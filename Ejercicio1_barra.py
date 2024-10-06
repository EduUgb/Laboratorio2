import matplotlib.pyplot as plt
import pandas as pd

"""
El siguiente gráfico muestra un análisis de la cantidad de jugadores por equipo nominados a balón de oro 2024.
"""
#Se cargan y leen los datos
df = pd.read_csv("BallonDor.csv")
frec  = df['team'].value_counts()

#Se crea una figura y un eje para el grafico, se le asigna un tamaño y se definen colores
fig, ax = plt.subplots(figsize=(6, 6))
colores = ["LightBlue", "Red", "Blue", "DarkRed", "SkyBlue", "DarkBlue", "RoyalBlue", "Black", "Gray", "Green"]


#Se crea un grafico de barras, se le asigna un titulo general y textos en el eje Y y X
ax.bar(frec.index, frec.values, color=colores) 
ax.set_title("Nominados a Balón de Oro 2024")
ax.set_ylabel("N° Nominados")
ax.set_xlabel("Equipos")
#Se rotan los textos de los equipos para que sean legibles y no se acumulen
ax.set_xticklabels(frec.index, rotation=45, ha="right")
#Se le cambia el color al fondo
ax.set_facecolor("LightYellow")


#Ajusta el diseño del grafico (margenes) para evitar acumulamiento  de texto y que se vea bien
plt.tight_layout()

#Muestra el gráfico
plt.show()