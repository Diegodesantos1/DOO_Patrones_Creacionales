# Importo la biblioteca Matplotlib para la visualización de datos y Pandas para el csv.
import matplotlib.pyplot as plt
import pandas as pd

# Defino una clase "VisualizacionHistograma" para realizar visualización de datos.


class VisualizacionHistograma:
    # El constructor de la clase recibe un objeto "data" que contiene los datos a visualizar.
    def __init__(self, data):
        self.data = data

    # Método "plot_graph" para generar y mostrar un gráfico de un tipo específico (histograma, barras, circular).
    def plot_graph(self, kind, title):
        # Genero el gráfico especificado (histograma, barras, circular).
        grafica = self.data.plot(kind=kind)
        grafica.set_title(title)
        grafica.set_xlabel('Valor')
        grafica.set_ylabel('Frecuencia')
        # Muestro el gráfico en la pantalla.
        plt.show()

    # Método "histograma" para generar y mostrar un gráfico de histograma.
    def histograma(self):
        self.plot_graph('hist', 'Histograma de {}'.format(self.data.name))

    # Método "barras" para generar y mostrar un gráfico de barras.
    def barras(self):
        self.plot_graph(
            'bar', 'Gráfico de barras de {}'.format(self.data.name))

    # Método "circular" para generar y mostrar un gráfico circular.
    def circular(self):
        self.plot_graph('pie', 'Gráfico circular de {}'.format(self.data.name))

    # Método "barras_frecuencia" para generar y mostrar un gráfico de barras de frecuencia.
    def barras_frecuencia(self, data, variable):
        data[variable] = data[variable].str.split(",").str[0]
        data[variable].value_counts().plot.bar()
        plt.title(f'Frecuencia de {variable} en las actividades')
        plt.show()

    # Método "circular_frecuencia" para generar y mostrar un gráfico circular de frecuencia.
    def circular_frecuencia(self, data, variable):
        data[variable] = data[variable].str.split(",").str[0]
        data[variable].value_counts().plot.pie()
        plt.title(f'Frecuencia de {variable} en las actividades')
        plt.show()
