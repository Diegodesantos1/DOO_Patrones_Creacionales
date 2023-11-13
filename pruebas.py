from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


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


class Pizza(Menu):

    def operation(self) -> str:
        return "Pizza"


class Bebida(Menu):

    def operation(self) -> str:
        return "Bebida"


class Postre(Menu):

    def operation(self) -> str:
        return "Postre"


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


def client_code(Menu: Menu) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {Menu.operation()}", end="")


def client_code2(Menu1: Menu, Menu2: Menu) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Menu class, the client code can work with any Menu, simple or complex,
    without depending on their concrete classes.
    """

    if Menu1.is_composite():
        Menu1.add(Menu2)

    print(f"RESULT: {Menu1.operation()}", end="")
    if Menu1.is_composite():
        Menu1.remove(Menu2)


if __name__ == "__main__":
    """
    This way the client code can support the simple leaf Menus...
    """

    simple = Pizza()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    """
    ...as well as the complex composites.
    """

    tree = Composite()
    branch1 = Composite()
    branch1.add(Pizza())
    branch1.add(Pizza())
    branch2 = Composite()
    branch2.add(Pizza())
    tree.add(branch1)
    tree.add(branch2)
    print("Client: Now I've got a composite Menu:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
