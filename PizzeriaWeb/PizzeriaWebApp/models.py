from django.db import models

# Create your models here.
class Pizza:
    next_order_number = 1

    def __init__(self, masa, salsa, ingredientes, tecnica, presentacion, maridaje, extras):
        self.numero_pedido = Pizza.next_order_number
        self.masa = masa
        self.salsa = salsa
        self.ingredientes = ingredientes
        self.tecnica = tecnica
        self.presentacion = presentacion
        self.maridaje = maridaje
        self.extras = extras
        Pizza.next_order_number += 1


class Ingredientes:
    def __init__(self):
        self.ingredientes_disponibles = [
            "Jamón", "Queso", "Champiñones", "Tomate", "Pimiento", "Cebolla", "Piña", "Pepperoni", "Salami", "Aceitunas",
            "Pollo", "Carne picada", "Chorizo", "Tocino", "Jalapeños"]
