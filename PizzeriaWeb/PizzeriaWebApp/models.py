from django.db import models

from abc import ABC, abstractmethod
from typing import List, Optional


class PizzaBuilder(ABC):
    @property
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
    def set_tamaño(self, tamaño: str) -> None:
        pass


class Pizza:
    def __init__(self, masa, salsa, ingredientes, tecnica, presentacion, maridaje, extras, tamaño):
        self.masa = masa
        self.salsa = salsa
        self.ingredientes = ingredientes
        self.tecnica = tecnica
        self.presentacion = presentacion
        self.maridaje = maridaje
        self.extras = extras
        self.tamaño = tamaño


class UsuarioBuilder(ABC):
    @abstractmethod
    def set_usuario(self, usuario: str) -> None:
        pass

    @abstractmethod
    def set_contraseña(self, contraseña: str) -> None:
        pass


class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña


class LoginBuilder(ABC):
    @abstractmethod
    def set_usuario(self, usuario: str) -> None:
        pass

    @abstractmethod
    def set_contraseña(self, contraseña: str) -> None:
        pass


class Login:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
