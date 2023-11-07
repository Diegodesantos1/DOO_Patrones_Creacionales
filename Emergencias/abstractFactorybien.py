from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from typing import Tuple


class FabricaCentral(ABC):
    @abstractmethod
    def crear_datos(self) -> Datos_Estadisticos:
        pass

    @abstractmethod
    def crear_graficos(self) -> Datos_Graficos:
        pass


# Fábrica concreta 1
class FabricaDatosNumericos(FabricaCentral):
    def crear_datos_texto(self) -> Datos_Estadisticos:
        return Media()

    def crear_datos_texto(self) -> Datos_Estadisticos:
        return Mediana()

    def crear_datos_texto(self) -> Datos_Estadisticos:
        return Moda()

    def crear_datos_texto(self) -> Datos_Estadisticos:
        return DesviacionTipica()

    def crear_datos_texto(self) -> Datos_Estadisticos:
        return Varianza()


# Fábrica concreta 2
class FabricaGrafica(FabricaCentral):
    def crear_graficos(self) -> Datos_Graficos:
        return Histograma()

    def crear_graficos(self) -> Datos_Graficos:
        return Circular()

    def crear_graficos(self) -> Datos_Graficos:
        return Barras()


# Producto abstracto A

class Datos_Estadisticos(ABC):
    @abstractmethod
    def useful_function_a(self) -> None:
        pass

# Producto concreto A1


class Media(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        return "La media es: " + str(numpy.mean(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))

# Producto concreto A2


class Mediana(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        return "La mediana es: " + str(numpy.median(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))

# Producto concreto A3


class Moda(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])
        mode_result = data.mode()
        if not mode_result.empty:
            mode_value = mode_result.iloc[0, 0]
            return f"La moda es: {mode_value}"
        else:
            return "No hay moda en los datos."

# Producto concreto A4


class DesviacionTipica(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])
        std_result = data.std(axis=0)
        return f"La desviación típica es: {std_result.iloc[0]}"

# Producto concreto A5


class Varianza(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])
        var_result = data.var(axis=0)
        return f"La varianza es: {var_result.iloc[0]}"


# Producto abstracto B

class Datos_Graficos(ABC):
    @abstractmethod
    def useful_function_a(self) -> None:
        pass

# Producto concreto B1
class Histograma(Datos_Graficos):
    def useful_function_a(self) -> None:
        columnas = ["DIAS", "CATEGORIA", "AUDIENCIA"]
        for columna in columnas:
            data = pd.read_csv(
                'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=[columna])

            if columna == "DIAS":
                data[columna] = data[columna].str.split(",").str[0]
                plt.hist(data, bins=10)
                plt.title('Histograma de {}'.format(columna))
                plt.xlabel(f"{columna}")
                plt.ylabel('Frecuencia')
                plt.show()
                print("Histograma de {}".format(columna))

# Producto concreto B2
class Circular(Datos_Graficos):
    def useful_function_a(self) -> None:
        columnas = ["DIAS", "CATEGORIA", "AUDIENCIA"]
        for columna in columnas:
            data = pd.read_csv(
                'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=[columna])
            frecuencias = data[columna].str.split(",").str[0].value_counts()
            labels = frecuencias.index
            sizes = frecuencias.values
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.title('Gráfico Circular de {}'.format(columna))
            plt.show()
            print("Gráfico Circular de {}".format(columna))

# Producto concreto B3
class Barras(Datos_Graficos):
    def useful_function_a(self) -> None:
        columnas = ["DIAS", "CATEGORIA", "AUDIENCIA"]
        for columna in columnas:
            data = pd.read_csv(
                'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=[columna])
            frecuencias = data[columna].str.split(",").str[0].value_counts()
            etiquetas = frecuencias.index
            alturas = frecuencias.values
            plt.bar(etiquetas, alturas)
            plt.title('Gráfico de Barras de {}'.format(columna))
            plt.xlabel(f"{columna}")
            plt.ylabel('Frecuencia')
            plt.show()
            print("Gráfico de Barras de {}".format(columna))



def client_code(factory: FabricaCentral) -> None:
    product_a = factory.crear_datos()
    product_b = factory.crear_graficos()

    print(product_a.useful_function_a(), end="")
    print(product_b.useful_function_b(), end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Cliente: Probando la fábrica de datos estadísticos:")
    client_code(FabricaDatosNumericos())
    print("Cliente: Probando la fábrica de gráficos:")
    client_code(FabricaGrafica())
