import matplotlib.pyplot as plt
import pandas as pd

#En este gráfico de pastel veremos el numero de reseñas que tienen algunos autos

#Aquí extraemos los datos del archivo csv
df = pd.read_csv("CARS_1.csv")

#Este es un limitante para que solo nos permita dar 10 resultados
topN = 10
dfTop = df.nlargest(topN, 'reviews_count')

#Aquí escogemos las columnas que usaremos para extraer sus datos
frec = dfTop['reviews_count']
autos = dfTop['car_name']
colores = ['#FF0000', '#32CD32', '#FF00FF', '#1ABC9C', '#F8E231', '#FFC67D', '#0097A7', '#C7B8EA', '#FFD7BE', '#4B0082']

#Creamos el gráfico circular o de pastel asignandole sus titulos respectivos
plt.pie(frec, labels = autos, autopct='%d', colors=colores)
plt.title("Número de reseñas de autos")
plt.show()