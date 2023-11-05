import pandas as pd
import matplotlib.pyplot as plt


class AbstractFactoryAnalisis:
    def create_analisis_estadistico(self, data):
        pass

    def create_visualizacion(self, data):
        pass


class FactoryEstadisticas(AbstractFactoryAnalisis):
    def create_analisis_estadistico(self, data):
        return AnalisisEstadistico(data)

    def create_visualizacion(self, data):
        return VisualizacionHistograma(data)


class AnalisisEstadistico:
    def __init__(self, data):
        self.data = data

    def calcular(self):
        media = self.data.mean()
        mediana = self.data.median()
        moda = self.data.mode().iloc[0]
        desviacion_tipica = self.data.std()
        varianza = self.data.var()

        return {
            "Media": media,
            "Mediana": mediana,
            "Moda": moda,
            "Desviación Típica": desviacion_tipica,
            "Varianza": varianza
        }


class VisualizacionHistograma:
    def __init__(self, data):
        self.data = data

    def histograma(self):
        grafica = self.data.plot.hist()
        grafica.set_title('Histograma de {}'.format(self.data.name))
        grafica.set_xlabel('Valor')
        grafica.set_ylabel('Frecuencia')
        plt.show()

    def barras(self):
        grafica = self.data.value_counts().plot.bar()
        grafica.set_title('Gráfico de barras de {}'.format(self.data.name))
        grafica.set_xlabel('Valor')
        grafica.set_ylabel('Frecuencia')
        plt.show()

    def circular(self):
        grafica = self.data.value_counts().plot.pie()
        grafica.set_title('Gráfico circular de {}'.format(self.data.name))
        grafica.set_xlabel('Valor')
        grafica.set_ylabel('Frecuencia')
        plt.show()


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


def client_code(factory: AbstractFactoryAnalisis) -> None:
    data = pd.read_csv('Emergencias/data/Emergencias_limpio.csv',
                       sep=';')

    columnas = ["DIAS", "CATEGORIA", "AUDIENCIA"]


    analisis = factory.create_analisis_estadistico(data["PRECIO"])
    visualizacion = factory.create_visualizacion(data["PRECIO"])
    print("Analisis de la columna {}".format("PRECIO"))
    print(analisis.calcular())
    visualizacion.histograma()
    visualizacion.barras()
    visualizacion.circular()
    print("-"*40)

    for columna in columnas:
        analisis = factory.create_analisis_estadistico(data[columna])
        visualizacion = factory.create_visualizacion(data[columna])
        print("Analisis de la columna {}".format(columna))
        visualizacion.barras_frecuencia(data, columna)
        visualizacion.circular_frecuencia(data, columna)
        print("-"*40)




if __name__ == "__main__":
    """
    El código del cliente puede trabajar con cualquier clase de fábrica concreta.
    """
    print("Cliente: Probando la fábrica estadística:")
    client_code(FactoryEstadisticas())
