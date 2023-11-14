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


class ComponenteMenu(ABC):

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def operation(self) -> str:
        pass


class Pizza_Menu(ComponenteMenu):
    def __init__(self, pizza):
        self.pizza = pizza

    def to_dict(self) -> dict:
        return {"type": "Pizza", "nombre": self.pizza}

    def operation(self) -> str:
        return f"Pizza: {self.pizza}"


class Bebida(ComponenteMenu):
    def __init__(self, bebida):
        self.bebida = bebida

    def to_dict(self) -> dict:
        return {"type": "Bebida", "nombre": self.bebida}

    def operation(self) -> str:
        return f"Bebida: {self.bebida}"


class Postre(ComponenteMenu):
    def __init__(self, postre):
        self.postre = postre

    def to_dict(self) -> dict:
        return {"type": "Postre", "nombre": self.postre}

    def operation(self) -> str:
        return f"Postre: {self.postre}"


class Entrante(ComponenteMenu):
    def __init__(self, entrante):
        self.entrante = entrante

    def to_dict(self) -> dict:
        return {"type": "Entrante", "nombre": self.entrante}

    def operation(self) -> str:
        return f"Entrante: {self.entrante}"


class MenuComposite(ComponenteMenu):

    def __init__(self, pizza, bebida, postre, entrante):
        self.entrate = entrante
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre

    def add(self, componente: ComponenteMenu) -> None:
        self._children.append(componente)

    def remove(self, componente: ComponenteMenu) -> None:
        self._children.remove(componente)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"Menu({', '.join(results)})"

    def to_dict(self) -> dict:
        results = [child.to_dict() for child in self._children]
        return {
            "type": "Composite",
            "children": results,
        }


class MenuIndividual(MenuComposite):

    def __init__(self, entrante, pizza, bebida, postre):
        self.entrante = entrante
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre



class MenuInfantil(MenuComposite):

    def __init__(self, entrante, pizza, bebida, postre, descuento):
        self.entrante = entrante
        self.pizza = pizza
        self.bebida = bebida
        self.postre = postre
        self.descuento = descuento

    def to_dict(self) -> dict:
        return {
            "nombre": "Infantil",
            "precio": 7.50,
            "entrante": self.entrante,
            "pizza": self.pizza,
            "bebida": self.bebida,
            "postre": self.postre,
            "descuento": self.descuento,
        }