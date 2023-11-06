# recommendations.py

class Recomendaciones:
    def __init__(self):
        self.recomendaciones = {}

    def generar_recomendaciones(self, pizza):
        if "Queso" in pizza.ingredientes:
            self.recomendaciones["Vino"] = "Recomendamos un vino tinto para acompañar tu pizza de queso."
