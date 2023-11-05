from factory import FactoryEstadisticas, client_code


if __name__ == "__main__":
    """
    El código del cliente puede trabajar con cualquier clase de fábrica concreta.
    """
    print("Cliente: Probando la fábrica estadística:")
    client_code(FactoryEstadisticas())
