from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class Proxy(Subject):
    def __init__(self, usuario_real, usuario, contraseña):
        self._usuario_real = usuario_real
        self._usuario = usuario
        self._contraseña = contraseña

    def obtener_usuario(self):
        return self._usuario

    def obtener_contraseña(self):
        return self._contraseña

    def request(self) -> None:
        if self.authenticate():
            self._usuario_real.request()
        else:
            print("Acceso denegado.")

    def authenticate(self) -> bool:
        usuario_introducido = input("Ingrese su nombre de usuario: ")
        contraseña_introducida = input("Ingrese su contraseña: ")

        if usuario_introducido == "admin" and contraseña_introducida == "admin":
            print("Acceso como admin.")
            return True
        elif usuario_introducido == self._usuario and contraseña_introducida == self._contraseña:
            print("Acceso autorizado.")
            return True
        else:
            print("Autenticación fallida. Acceso denegado.")
            return False
