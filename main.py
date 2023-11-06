import os
eleccion =int(input("¿Qué ejercicio quieres ejecutar?\n1 --> Emergencias\n2 --> Pizzeria\n"))

if eleccion == 1:
    from Emergencias.main import *
    if __name__ == "__main__":
        print("Cliente: Probando la fábrica estadística:")
        client_code(FactoryEstadisticas())

elif eleccion == 2:
    eleccion2 = int(input("¿Qué ejercicio quieres ejecutar?\n1 --> Terminal\n2 --> Interfaz Gráfica\n3 --> Django\n"))

    if eleccion2 == 1:
        from Pizzeria.main import *
        if __name__ == "__main__":
            ejecutar_pizzeria()

    elif eleccion2 == 2:
        if __name__ == "__main__":
            import Pizzeria.interfaz
            Pizzeria.interfaz.main()

    elif eleccion2 == 3:
        os.system("cd PizzeriaWeb")
        os.system("python manage.py runserver")
