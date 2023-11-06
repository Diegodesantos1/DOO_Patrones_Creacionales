# Importo la biblioteca Pandas para trabajar con el csv.
import pandas as pd

# Defino una clase "AnalisisEstadistico" para realizar análisis estadísticos.


class AnalisisEstadistico:
    # El constructor de la clase recibe un objeto "data" que contiene los datos a analizar.
    def __init__(self, data):
        # Guardo los datos en un atributo de la clase.
        self.data = data

    # Método "calcular" para realizar el análisis estadístico.
    def calcular(self):
        # Calculo estadísticas descriptivas del conjunto de datos.
        media = self.data.mean()
        mediana = self.data.median()
        moda = self.data.mode().iloc[0]
        desviación_tipica = self.data.std()
        varianza = self.data.var()

        # Retorno un diccionario con las estadísticas calculadas.
        return {
            "Media": media,
            "Mediana": mediana,
            "Moda": moda,
            "Desviación Típica": desviación_tipica,
            "Varianza": varianza
        }
