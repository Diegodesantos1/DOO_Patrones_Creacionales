# Importo la biblioteca Pandas para trabajar con el csv.
import pandas as pd

# Importo las clases y funciones necesarias desde los módulos correspondientes.
from Emergencias.analysis.abstract_factory import AbstractFactoryAnalisis
from Emergencias.analysis.statistics import AnalisisEstadistico
from Emergencias.analysis.visualization import VisualizacionHistograma

# Defino una subclase de "AbstractFactoryAnalisis" llamada "FactoryEstadisticas".


class FactoryEstadisticas(AbstractFactoryAnalisis):
    def create_analisis_estadistico(self, data):
        # Creo una instancia de "AnalisisEstadistico" y la retorno.
        return AnalisisEstadistico(data)

    def create_visualizacion(self, data):
        # Creo una instancia de "VisualizacionHistograma" y la retorno.
        return VisualizacionHistograma(data)

# Defino una función llamada "client_code" que toma una fábrica como argumento.
# La función realizará análisis estadísticos y visualización de datos.


def client_code(factory: AbstractFactoryAnalisis) -> None:
    # Leo un archivo CSV y cargo los datos en un DataFrame de Pandas.
    data = pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';')

    # Defino una lista de nombres de columnas en las que se realizarán análisis.
    columnas = ["DIAS", "CATEGORIA", "AUDIENCIA"]

    # Realizo análisis y visualización de la columna "PRECIO(€)".
    analisis = factory.create_analisis_estadistico(data["PRECIO(€)"])
    visualizacion = factory.create_visualizacion(data["PRECIO(€)"])

    # Calculo estadísticas y las imprimo en la consola.
    print("Análisis de la columna {}".format("PRECIO(€)"))
    print(analisis.calcular())

    # Genero y muestro gráficos de histograma, barras y circular.
    visualizacion.histograma()
    visualizacion.barras()
    visualizacion.circular()
    print("-" * 40)

    # Realizo análisis y visualización de las columnas en "columnas".
    for columna in columnas:
        analisis = factory.create_analisis_estadistico(data[columna])
        visualizacion = factory.create_visualizacion(data[columna])

        # Genero y muestro gráficos de barras y circular de frecuencia.
        print("Análisis de la columna {}".format(columna))
        visualizacion.barras_frecuencia(data, columna)
        visualizacion.circular_frecuencia(data, columna)
        print("-" * 40)
