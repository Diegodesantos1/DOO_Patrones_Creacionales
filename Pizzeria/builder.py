# builders.py

from Pizzeria.models import Pizza

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def select_masa(self, masa):
        self.pizza.masa = masa

    def select_salsa(self, salsa):
        self.pizza.salsa = salsa

    def add_ingrediente(self, ingrediente):
        self.pizza.ingredientes.append(ingrediente)

    def select_tecnica_coccion(self, tecnica):
        self.pizza.tecnica_coccion = tecnica

    def select_presentacion(self, presentacion):
        self.pizza.presentacion = presentacion

    def select_maridaje(self, maridaje):
        self.pizza.maridaje = maridaje

    def add_extra(self, extra):
        self.pizza.extras.append(extra)

    def build(self):
        return self.pizza
