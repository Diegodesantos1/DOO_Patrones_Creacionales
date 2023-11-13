import unittest


from GestionDocumentalSAMUR.tests import *
"""if __name__ == '__main__':
    unittest.main()"""

from GestionDocumentalSAMUR.estructura import Carpeta, Imagen, DocumentoTexto

# Crear instancias de la imagen y el documento de texto
imagen = Imagen("Ambulancia_Madrid.jpg", "/GestionDocumentalSAMUR/archivos/ambulancia_madrid.jpg")
documento_texto = DocumentoTexto("prueba.txt", "Hola")

# Crear una carpeta y modificar su contenido
carpeta = Carpeta("MiCarpeta")
carpeta.modificar_contenido([imagen, documento_texto])

# Imprimir el contenido de la carpeta para verificar que la modificación fue exitosa
print("Contenido de la carpeta:", carpeta.obtener_contenido())
