from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import numpy
import matplotlib.pyplot as plt


class FabricaCentral(ABC):
    @abstractmethod
    def crear_datos(self) -> Datos_Estadisticos:
        pass

    @abstractmethod
    def crear_graficos(self) -> Datos_Graficos:
        pass

# Fábrica concreta 1


class FabricaDatosNumericos(FabricaCentral):
    def crear_datos(self) -> Datos_Estadisticos:
        return Media()

    def crear_graficos(self) -> Datos_Graficos:
        return Histograma()

# Fábrica concreta 2


class FabricaGrafica(FabricaCentral):
    def crear_datos(self) -> Datos_Estadisticos:
        return Mediana()

    def crear_graficos(self) -> Datos_Graficos:
        return Circular()


# Producto abstracto A

class Datos_Estadisticos(ABC):
    @abstractmethod
    def mostrar_datos(self) -> str:
        pass

# Producto concreto A1


class Media(Datos_Estadisticos):
    def mostrar_datos(self) -> str:
        return "La media es: " + str(numpy.mean(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))

# Producto concreto A2

class Mediana(Datos_Estadisticos):
    def mostrar_datos(self) -> str:
        return "La mediana es: " + str(numpy.median(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))
# Producto concreto A3


class Moda(Datos_Estadisticos):
    def mostrar_datos(self) -> str:
        return "La moda es: " + str(numpy.mode(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))

# Producto concreto A4


class Desviacion(Datos_Estadisticos):
    def mostrar_datos(self) -> str:
        return "La desviacion es: " + str(numpy.std(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))

# Producto concreto A5

class Varianza(Datos_Estadisticos):
    def mostrar_datos(self) -> str:
        return "La varianza es: " + str(numpy.var(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))
# Producto abstracto B


class Datos_Graficos(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

# Producto concreto B1


class Histograma(Datos_Graficos):
    def useful_function_b(self) -> None:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=["DIAS"])
        data["DIAS"] = data["DIAS"].str.split(",").str[0]
        plt.hist(data, bins=10)
        plt.title('Histograma de {}'.format("DIAS"))
        plt.xlabel('Dias')
        plt.ylabel('Frecuencia')
        plt.show()
        return "Histograma de {}".format("DIAS")

# Producto concreto B2


class Circular(Datos_Graficos):
    def useful_function_b(self) -> None:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=["CATEGORIA"])
        frecuencias = data["CATEGORIA"].str.split(",").str[0].value_counts()
        labels = frecuencias.index
        sizes = frecuencias.values
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Gráfico Circular de {}'.format("CATEGORIA"))
        plt.show()
        return "Gráfico Circular de {}".format("CATEGORIA")


def client_code(factory: FabricaCentral) -> None:
    product_a = factory.crear_datos()
    product_b = factory.crear_graficos()

    print(f"{product_a.mostrar_datos()}")
    print(f"{product_b.useful_function_b()}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Cliente: Probando la fábrica de datos estadísticos:")
    client_code(FabricaDatosNumericos())
    print("Cliente: Probando la fábrica de gráficos:")
    client_code(FabricaGrafica())
