import matplotlib.pyplot as plt
import pandas as pd

class VisualizacionHistograma:
    def __init__(self, data):
        self.data = data

    def plot_graph(self, kind, title):
        grafica = self.data.plot(kind=kind)
        grafica.set_title(title)
        grafica.set_xlabel('Valor')
        grafica.set_ylabel('Frecuencia')
        plt.show()

    def histograma(self):
        self.plot_graph('hist', 'Histograma de {}'.format(self.data.name))

    def barras(self):
        self.plot_graph('bar', 'Gráfico de barras de {}'.format(self.data.name))

    def circular(self):
        self.plot_graph('pie', 'Gráfico circular de {}'.format(self.data.name))

    def barras_frecuencia(self, data, variable):
        data[variable] = data[variable].str.split(",").str[0]
        data[variable].value_counts().plot.bar()
        plt.title(f'Frecuencia de {variable} en las actividades')
        plt.show()

    def circular_frecuencia(self, data, variable):
        data[variable] = data[variable].str.split(",").str[0]
        data[variable].value_counts().plot.pie()
        plt.title(f'Frecuencia de {variable} en las actividades')
        plt.show()
