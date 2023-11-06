# utils.py

# Función para calcular el tiempo de cocción de una pizza en minutos
def calcular_tiempo_coccion(pizza):
    tiempo = 0
    if pizza.masa == "Delgada":
        tiempo += 10
    elif pizza.masa == "Pan":
        tiempo += 15
    elif pizza.masa == "Fermentada":
        tiempo += 20
    tiempo += len(pizza.ingredientes) * 2  # 2 minutos por ingrediente
    return tiempo

# Función para verificar si una pizza es vegetariana
def es_pizza_vegetariana(pizza):
    ingredientes_no_vegetarianos = ["Jamón", "Pepperoni", "Pollo", "Carne picada", "Salami", "Chorizo", "Tocino"]
    for ingrediente in pizza.ingredientes:
        if ingrediente in ingredientes_no_vegetarianos:
            return False
    return True

# Función para calcular el precio de una pizza
def calcular_precio_pizza(pizza):
    precio = 0
    if pizza.masa == "Delgada":
        precio += 5
    elif pizza.masa == "Pan":
        precio += 8
    elif pizza.masa == "Fermentada":
        precio += 10
    precio += len(pizza.ingredientes) * 1.5  # $1.50 por ingrediente
    return precio
