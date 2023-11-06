import pandas as pd
from Emergencias.analysis.abstract_factory import AbstractFactoryAnalisis
from Emergencias.analysis.statistics import AnalisisEstadistico
from Emergencias.analysis.visualization import VisualizacionHistograma

class FactoryEstadisticas(AbstractFactoryAnalisis):
    def create_analisis_estadistico(self, data):
        return AnalisisEstadistico(data)

    def create_visualizacion(self, data):
        return VisualizacionHistograma(data)

def client_code(factory: AbstractFactoryAnalisis) -> None:
    data = pd.read_csv('Emergencias/data/Emergencias_limpio.csv',
                       sep=';')

    columnas = ["DIAS", "CATEGORIA", "AUDIENCIA"]

    analisis = factory.create_analisis_estadistico(data["PRECIO(€)"])
    visualizacion = factory.create_visualizacion(data["PRECIO(€)"])
    print("Analisis de la columna {}".format("PRECIO(€)"))
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
