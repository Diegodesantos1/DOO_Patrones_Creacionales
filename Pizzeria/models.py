# models.py

class Pizza:
    next_order_number = 1

    def __init__(self):
        self.numero_pedido = None
        self.masa = None
        self.salsa = None
        self.ingredientes = []
        self.tecnica_coccion = None
        self.presentacion = None
        self.maridaje = None
        self.extras = []


class Ingredientes:
    def __init__(self):
        self.ingredientes_disponibles = [
            "Jamón", "Queso", "Champiñones", "Tomate", "Pimiento", "Cebolla", "Piña", "Pepperoni", "Salami", "Aceitunas",
            "Pollo", "Carne picada", "Chorizo", "Tocino", "Jalapeños"]
