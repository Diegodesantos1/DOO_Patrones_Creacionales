# price.py
from .models import Pizza

class Precios:
    def __init__(self, file_path):
        self.file_path = file_path

    def calcular_precio(self, pizza):
        precio = 0

        if pizza.tamaño == "Pequeña":
            precio += 4
        elif pizza.tamaño == "Mediana":
            precio += 5
        elif pizza.tamaño == "Grande":
            precio += 6
        elif pizza.tamaño == "Familiar":
            precio += 7

        # Assuming pizza.ingredientes and pizza.extras are lists
        precio += len(pizza.ingredientes) * 0.75
        precio += len(pizza.extras) * 1.50

        return precio
