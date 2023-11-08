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
        self.masa = masa
        self.salsa = salsa
        self.ingredientes = ingredientes
        self.tecnica = tecnica
        self.presentacion = presentacion
        self.maridaje = maridaje
        self.extras = extras
