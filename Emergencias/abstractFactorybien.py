from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import numpy
from typing import Tuple


class FabricaCentral(ABC):
    @abstractmethod
    def crear_datos_texto(self) -> Datos_Estadisticos:
        pass


class FabricaDatosNumericos(FabricaCentral):
    def crear_datos_texto(self) -> Tuple[Datos_Estadisticos, Datos_Estadisticos, Datos_Estadisticos, Datos_Estadisticos, Datos_Estadisticos]:
        return (Media(), Mediana(), Moda(), DesviacionTipica(), Varianza())


class FabricaGraficas(FabricaCentral):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def crear_media(self) -> Datos_Estadisticos:
        return Media()

    def crear_mediana(self) -> Datos_Estadisticos:
        return Mediana()

    def crear_moda(self) -> Datos_Estadisticos:
        return Moda()

    def crear_desviacion_tipica(self) -> Datos_Estadisticos:
        return DesviacionTipica()

    def crear_varianza(self) -> Datos_Estadisticos:
        return Varianza()


class Datos_Estadisticos(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class Media(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        return "La media es: " + str(numpy.mean(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))


class Mediana(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        return "La mediana es: " + str(numpy.median(pd.read_csv('Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])))


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


class DesviacionTipica(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])
        std_result = data.std(axis=0)
        return f"La desviación típica es: {std_result.iloc[0]}"


class Varianza(Datos_Estadisticos):
    def useful_function_a(self) -> str:
        data = pd.read_csv(
            'Emergencias/data/Emergencias_limpio.csv', sep=';', usecols=['PRECIO(€)'])
        var_result = data.var(axis=0)
        return f"La varianza es: {var_result.iloc[0]}"


def client_code(factory: FabricaCentral) -> None:
    datos_texto = factory.crear_datos_texto()
    for dato in datos_texto:
        print(f"Datos estadísticos: {dato.useful_function_a()}", end="\n")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Cliente: Probando la fábrica de datos estadísticos:")
    client_code(FabricaDatosNumericos())
