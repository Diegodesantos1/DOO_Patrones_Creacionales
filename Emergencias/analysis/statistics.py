import pandas as pd

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
