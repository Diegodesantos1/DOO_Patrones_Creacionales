from django.db import models

from abc import ABC, abstractmethod
from typing import List, Optional


class PizzaBuilder(ABC):
    @abstractmethod
    def set_masa(self, masa: str) -> None:
        pass

    @abstractmethod
    def set_salsa(self, salsa: str) -> None:
        pass

    @abstractmethod
    def set_ingredientes(self, ingredientes: List[str]) -> None:
        pass

    @abstractmethod
    def set_tecnica(self, tecnica: str) -> None:
        pass

    @abstractmethod
    def set_presentacion(self, presentacion: str) -> None:
        pass

    @abstractmethod
    def set_maridaje(self, maridaje: Optional[str]) -> None:
        pass

    @abstractmethod
    def set_extras(self, extras: List[str]) -> None:
        pass

    @abstractmethod
    def build(self) -> 'Pizza':
        pass


class Pizza:
    def __init__(self, masa, salsa, ingredientes, tecnica, presentacion, maridaje, extras):
        self.numero_pedido = None
        self.masa = masa
        self.salsa = salsa
        self.ingredientes = ingredientes
        self.tecnica = tecnica
        self.presentacion = presentacion
        self.maridaje = maridaje
        self.extras = extras


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def build_pizza(self) -> Pizza:
        self.builder.set_masa("Delgada")
        self.builder.set_salsa("Tomate")
        self.builder.set_ingredientes(["Queso"])
        self.builder.set_tecnica("Horno tradicional")
        self.builder.set_presentacion("Clásica")
        self.builder.set_maridaje("Vino")
        self.builder.set_extras(["Orégano", "Aceitunas"])

        return self.builder.build()

# Ejemplo de uso


class PizzaChef(PizzaBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = Pizza("", "", [], "", "", None, [])

    def set_masa(self, masa: str):
        self.pizza.masa = masa

    def set_salsa(self, salsa: str):
        self.pizza.salsa = salsa

    def set_ingredientes(self, ingredientes: List[str]):
        self.pizza.ingredientes = ingredientes

    def set_tecnica(self, tecnica: str):
        self.pizza.tecnica = tecnica

    def set_presentacion(self, presentacion: str):
        self.pizza.presentacion = presentacion

    def set_maridaje(self, maridaje: Optional[str]):
        self.pizza.maridaje = maridaje

    def set_extras(self, extras: List[str]):
        self.pizza.extras = extras

    def build(self) -> Pizza:
        return self.pizza