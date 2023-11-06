# main.py
from colorama import init, Fore, Back, Style
import os
from models import Pizza, Ingredientes
from recommendations import Recomendaciones
from storage import CSVStorage
from utils import calcular_tiempo_coccion, es_pizza_vegetariana, calcular_precio_pizza
from builder import PizzaBuilder

if __name__ == "__main__":
    # Crear instancias de las clases necesarias
    ingredientes = Ingredientes()
    recomendaciones = Recomendaciones()
    storage = CSVStorage('pizzas.csv')
    # Interacción con el usuario
    print(Fore.CYAN + "¡Bienvenido a Diego's Pizzeria! Crea tu propia pizza personalizada." + Style.RESET_ALL)

    # Crear una nueva pizza utilizando el PizzaBuilder
    pizza_builder = PizzaBuilder()

    masa = input(Fore.LIGHTGREEN_EX +"Elige el tipo de masa (Delgada, Pan, Fermentada): " + Style.RESET_ALL)
    pizza_builder.select_masa(masa)

    salsa = input(Fore.LIGHTRED_EX + "Elige la salsa base (Tomate, Pesto, BBQ): " + Style.RESET_ALL)
    pizza_builder.select_salsa(salsa)

    print(Fore.LIGHTMAGENTA_EX +"Añade ingredientes a tu pizza (ingresa 'fin' para terminar):")
    while True:
        ingrediente = input("Ingrediente: ")
        if ingrediente == 'fin':
            break
        if ingrediente in ingredientes.ingredientes_disponibles:
            pizza_builder.add_ingrediente(ingrediente)
        else:
            print("Ingrediente no disponible. Inténtalo de nuevo.")

    tecnica_coccion = input(
        "Elige la técnica de cocción (Horno tradicional, Cocina a la leña, Cocina molecular): ")
    pizza_builder.select_tecnica_coccion(tecnica_coccion)

    presentacion = input(
        Fore.LIGHTGREEN_EX + "Elige la presentación de la pizza (Clásica, Artística, Personalizada): ")
    pizza_builder.select_presentacion(presentacion)

    maridaje = input(Fore.LIGHTYELLOW_EX + "Elige el maridaje (Vino, Cerveza, Coctel): ")
    pizza_builder.select_maridaje(maridaje)

    print("Añade extras a tu pizza (ingresa 'fin' para terminar):")
    while True:
        extra = input("Extra: ")
        if extra == 'fin':
            break
        pizza_builder.add_extra(extra)

    # Construir la pizza
    pizza_personalizada = pizza_builder.build()

    # Generar recomendaciones
    recomendaciones.generar_recomendaciones(pizza_personalizada)

    # Calcular el tiempo de cocción
    tiempo_coccion = calcular_tiempo_coccion(pizza_personalizada)

    # Verificar si es una pizza vegetariana
    es_vegetariana = es_pizza_vegetariana(pizza_personalizada)

    # Calcular el precio de la pizza
    precio = calcular_precio_pizza(pizza_personalizada)
    # Guardar la pizza en el archivo CSV
    storage.guardar_pizza(pizza_personalizada)

    # Imprimir detalles de la pizza y recomendaciones
    os.system('cls')
    print(Fore.CYAN + "¡Tu pizza está lista!" + Style.RESET_ALL)
    print(f"Tiempo de Cocción: {tiempo_coccion} minutos")
    print(f"¿Es vegetariana? {'Sí' if es_vegetariana else 'No'}")
    print("Detalles de la pizza:")
    print(pizza_personalizada)

    print("Recomendaciones:")
    for key, value in recomendaciones.recomendaciones.items():
        print(f"{key}: {value}")

    print(f"El precio de la pizza es: ${precio}")
