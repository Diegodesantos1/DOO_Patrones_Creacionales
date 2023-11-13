from __future__ import annotations
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


class Menu(ABC):
    """
    The base Menu class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Menu:
        return self._parent

    @parent.setter
    def parent(self, parent: Menu):
        """
        Optionally, the base Menu can declare an interface for setting and
        accessing a parent of the Menu in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Menu class. This way, you won't need to
    expose any concrete Menu classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the Pizza-level Menus.
    """

    def add(self, Menu: Menu) -> None:
        pass

    def remove(self, Menu: Menu) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        Menu can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:

        pass


class MenuIndividual(Menu):

    def __init__(self, pizza, bebida, postre):
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre


class MenuDoble(Menu):

    def __init__(self, pizza, bebida, postre):
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre


class MenuTriple(Menu):

    def __init__(self, pizza, bebida, postre):
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre


class MenuFamiliar(Menu):

    def __init__(self, pizza, bebida, postre):
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre


class Composite(Menu):

    def __init__(self) -> None:
        self._children: List[Menu] = []

    def add(self, Menu: Menu) -> None:
        self._children.append(Menu)
        Menu.parent = self

    def remove(self, Menu: Menu) -> None:
        self._children.remove(Menu)
        Menu.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

    def to_dict(self) -> dict:
        results = [child.to_dict() for child in self._children]
        return {
            "type": "Composite",
            "children": results,
        }
