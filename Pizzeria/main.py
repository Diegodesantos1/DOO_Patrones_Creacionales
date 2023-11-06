# main.py

from models import Pizza, Ingredientes
from recommendations import Recomendaciones
from storage import CSVStorage
from utils import calcular_tiempo_coccion, es_pizza_vegetariana, EventLogger
from builder import PizzaBuilder

if __name__ == "__main__":
    # Crear instancias de las clases necesarias
    ingredientes = Ingredientes()
    recomendaciones = Recomendaciones()
    storage = CSVStorage('pizzas.csv')
    logger = EventLogger('event_log.txt')

    # Interacción con el usuario
    print("¡Bienvenido a Delizioso! Crea tu propia pizza personalizada.")

    # Crear una nueva pizza utilizando el PizzaBuilder
    pizza_builder = PizzaBuilder()

    masa = input("Elige el tipo de masa (Delgada, Pan, Fermentada): ")
    pizza_builder.select_masa(masa)

    salsa = input("Elige la salsa base (Tomate, Pesto, BBQ): ")
    pizza_builder.select_salsa(salsa)

    print("Añade ingredientes a tu pizza (ingresa 'fin' para terminar):")
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
        "Elige la presentación de la pizza (Clásica, Artística, Personalizada): ")
    pizza_builder.select_presentacion(presentacion)

    maridaje = input("Elige el maridaje (Vino, Cerveza, Coctel): ")
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

    # Guardar la pizza en el archivo CSV
    storage.guardar_pizza(pizza_personalizada)

    # Imprimir detalles de la pizza y recomendaciones
    print("Tu pizza personalizada:")
    print(f"Número de Pedido: {pizza_personalizada.numero_pedido}")
    print(f"Masa: {pizza_personalizada.masa}")
    print(f"Salsa: {pizza_personalizada.salsa}")
    print(f"Ingredientes: {', '.join(pizza_personalizada.ingredientes)}")
    print(f"Técnica de Cocción: {pizza_personalizada.tecnica_coccion}")
    print(f"Presentación: {pizza_personalizada.presentacion}")
    print(f"Maridaje: {pizza_personalizada.maridaje}")
    print(f"Extras: {', '.join(pizza_personalizada.extras)}")
    print(f"Tiempo de Cocción: {tiempo_coccion} minutos")
    print(f"¿Es vegetariana? {'Sí' if es_vegetariana else 'No'}")

    print("Recomendaciones:")
    for key, value in recomendaciones.recomendaciones.items():
        print(f"{key}: {value}")

    print("¡Gracias por crear tu pizza personalizada!")
