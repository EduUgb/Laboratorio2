import matplotlib.pyplot as ptl
import pandas as pd

"""
Este grafico es para ver los jugadores que más puntos anotaron en la season 2021-2022 de la NBA
"""
#Se cargan y leen los datos
df = pd.read_csv("2023_nba_player_stats.csv")

topN = 20
dfTop = df.nlargest(topN, 'PTS')

frec  = dfTop['PTS']
names = dfTop['PName']

#Se crea una figura y un eje para el grafico, se le asigna un tamaño y se definen colores
fig, ax = ptl.subplots(figsize=(6, 6))


#Se crea un grafico de barras, se le asigna un titulo general y textos en el eje Y y X
ax.plot(names,frec) 
ax.set_title("Máximos anotadores 2023 NBA")
ax.set_ylabel("Points")
ax.set_xlabel("Players names")
#Se rotan los textos de los equipos para que sean legibles y no se acumulen
ax.set_xticklabels(names, rotation=45, ha="right")


#Ajusta el diseño del grafico (margenes) para evitar acumulamiento  de texto y que se vea bien
ptl.tight_layout()

#Muestra el gráfico
ptl.show()