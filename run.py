import os
import unittest
os.system("pip install -r requirements.txt")
eleccion =int(input("¿Qué ejercicio quieres ejecutar?\n1 --> Emergencias\n2 --> Pizzeria\n"))

if eleccion == 1:
    from Emergencias.abstractFactorybien import *
    if __name__ == "__main__":
        print("Cliente: Probando la fábrica de datos estadísticos:")
        client_code(FabricaDatosNumericos())
        print("\nCliente: Probando la fábrica de gráficos:")
        client_code(FabricaGrafica())


elif eleccion == 2:
    print("Ejecutando servidor Django...")
    os.system("python PizzeriaWeb/manage.py runserver")

elif eleccion ==3:
    from GestionDocumentalSAMUR.tests import *
    if __name__ == '__main__':
        unittest.main()