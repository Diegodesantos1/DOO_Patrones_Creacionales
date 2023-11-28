import os

os.system("pip install -r requirements.txt")
eleccion = int(
    input("¿Qué ejercicio quieres ejecutar?\n1 --> Emergencias\n2 --> Pizzeria\n3 --> Gestión de archivos\n"))

if eleccion == 1:
    os.system("cls")
    from Emergencias.abstractFactorybien import *
    print("Cliente: Probando la fábrica de datos estadísticos:")
    client_code(FabricaDatosNumericos())
    print("\nCliente: Probando la fábrica de gráficos:")
    client_code(FabricaGrafica())


elif eleccion == 2:
    print("Ejecutando servidor Django...")
    os.system("python PizzeriaWeb/manage.py runserver")

elif eleccion == 3:
    os.system("cls")
    from Emergencias.funciones import *
    main_proxy()