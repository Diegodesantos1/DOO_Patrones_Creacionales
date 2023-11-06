# Importo las clases y funciones necesarias desde el módulo "Emergencias.client".
from Emergencias.client import FactoryEstadisticas, client_code

# Verifico si este archivo es el punto de entrada principal.
if __name__ == "__main__":
    # Imprimo un mensaje para indicar que estoy probando la fábrica estadística.
    print("Cliente: Probando la fábrica estadística:")

    # Llamo a la función "client_code" con una instancia de la fábrica "FactoryEstadisticas" como argumento.
    client_code(FactoryEstadisticas())
