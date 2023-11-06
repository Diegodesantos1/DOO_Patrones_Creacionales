eleccion =int(input("¿Qué ejercicio quieres ejecutar?\nEmergencias\nPizzeria\n"))

if eleccion == 1:
    from Emergencias.main import *
    if __name__ == "__main__":
        print("Cliente: Probando la fábrica estadística:")
        client_code(FactoryEstadisticas())

elif eleccion == 2:
    pass