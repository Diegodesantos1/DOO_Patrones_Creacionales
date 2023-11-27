import json
from abc import ABC, abstractmethod


class ArchivoSAMUR(ABC):
    @abstractmethod
    def obtener_nombre(self):
        pass

    @abstractmethod
    def obtener_tamaño(self):
        pass

    def agregar_documento(self, documento):
        pass

    def eliminar_documento(self, documento):
        pass

    def obtener_documento(self, nombre):
        pass


class Documento(ArchivoSAMUR):
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño

    def obtener_nombre(self):
        return self.nombre

    def obtener_tamaño(self):
        return self.tamaño

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'tipo': self.tipo,
            'tamaño': self.tamaño
        }


class Carpeta(ArchivoSAMUR):
    def __init__(self, nombre, tipo, contenido=None):
        self.nombre = nombre
        self.tipo = tipo
        if contenido is None:
            contenido = []
        self.contenido = contenido

    def obtener_nombre(self):
        return self.nombre

    def obtener_contenido(self):
        return self.contenido

    def obtener_tipo(self):
        return self.tipo

    def obtener_tamaño(self):
        total_tamaño = 0
        for documento in self.contenido:
            total_tamaño += documento.obtener_tamaño()
        return total_tamaño

    def obtener_documento(self, nombre):
        for documento in self.contenido:
            if isinstance(documento, Documento) and documento.obtener_nombre() == nombre:
                return documento
        return None

    def obtener_carpeta(self, nombre):
        if self.nombre == nombre:
            return self

        for elemento in self.contenido:
            if isinstance(elemento, Carpeta):
                carpeta_encontrada = elemento.obtener_carpeta(nombre)
                if carpeta_encontrada:
                    return carpeta_encontrada
        return None

    def agregar_documento(self, documento):
        self.contenido.append(documento)

    def eliminar_documento(self, nombre):
        for documento in self.contenido:
            if isinstance(documento, Documento) and documento.obtener_nombre() == nombre:
                self.contenido.remove(documento)
                print(f"Documento '{nombre}' eliminado con éxito.")
                return
        print(f"No se encontró el documento '{nombre}' en esta carpeta.")

    def modificar_documento(self, nombre_documento, atributo, nuevo_valor):
        documento = self.obtener_documento(nombre_documento)
        if documento:
            if atributo == "nombre":
                documento.nombre = nuevo_valor
            elif atributo == "tipo":
                documento.tipo = nuevo_valor
            elif atributo == "tamaño":
                documento.tamaño = nuevo_valor

            print(f"Documento '{nombre_documento}' modificado exitosamente.")
            return True
        else:
            print(f"No se encontró el documento '{
                  nombre_documento}' en esta carpeta.")
            return False

    def agregar_carpeta(self, carpeta):
        self.contenido.append(carpeta)

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'tipo': self.tipo,
            'contenido': [elemento.to_dict() for elemento in self.contenido]
        }


class Enlace(ArchivoSAMUR):
    def __init__(self, nombre, tipo, url):
        self.nombre = nombre
        self.tipo = tipo
        self.url = url

    def obtener_nombre(self):
        return self.nombre

    def obtener_url(self):
        return self.url

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'tipo': self.tipo,
            'url': self.url
        }
