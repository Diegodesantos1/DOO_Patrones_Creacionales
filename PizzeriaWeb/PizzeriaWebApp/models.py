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


class Masa(models.Model):
    @classmethod
    def masas_disponibles(cls):
        return [
            ("Delgada", "Delgada"),
            ("Pan", "Pan"),
            ("Fermentada", "Fermentada"),
            ("Sin gluten", "Sin gluten")

        ]


class Salsa(models.Model):
    @classmethod
    def salsas_disponibles(cls):
        return [
            ("Tomate", "Tomate"),
            ("Pesto", "Pesto"),
            ("BBQ", "BBQ"),
            ("Yogur", "Yogur"),
            ("Carbonara", "Carbonara"),
            ("Sin salsa", "Sin salsa"),
        ]

# Haz lo mismo para las otras clases (Ingredientes, Tecnica, Presentacion, Maridaje).


class Tecnica(models.Model):
    @classmethod
    def tecnicas_disponibles(cls):
        return [
            ("Horno tradicional", "Horno tradicional"),
            ("Cocina a la leña", "Cocina a la leña"),
            ("Cocina molecular", "Cocina molecular"),
        ]


class Presentacion(models.Model):
    @classmethod
    def presentaciones_disponibles(cls):
        return [
            ("Clásica", "Clásica"),
            ("Artística", "Artística"),
            ("Personalizada", "Personalizada"),
        ]


class Maridaje(models.Model):
    @classmethod
    def maridajes_disponibles(cls):
        return [
            ("Vino", "Vino"),
            ("Cerveza", "Cerveza"),
            ("Coctel", "Coctel"),
        ]


class Ingredientes(models.Model):
    @classmethod
    def ingredientes_disponibles(cls):
        return [
            ("Jamón", "Jamón"),
            ("Queso", "Queso"),
            ("Champiñones", "Champiñones"),
            ("Tomate", "Tomate"),
            ("Pimiento", "Pimiento"),
            ("Cebolla", "Cebolla"),
            ("Piña", "Piña"),
            ("Pepperoni", "Pepperoni"),
            ("Salami", "Salami"),
            ("Aceitunas", "Aceitunas"),
            ("Pollo", "Pollo"),
            ("Carne picada", "Carne picada"),
            ("Chorizo", "Chorizo"),
            ("Tocino", "Tocino"),
            ("Jalapeños", "Jalapeños"),
        ]
