# storage.py:
import csv
from .models import Pizza, Usuario, MenuComposite
from .price import Precios
from decimal import Decimal


class CSVStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_pizza(self, pizza):
        # Abre el archivo en modo 'a' (append) para agregar la pizza
        with open(self.file_path, mode='a', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                pizza.masa,
                pizza.salsa,
                ', '.join(pizza.ingredientes),
                pizza.tecnica,
                pizza.presentacion,
                pizza.maridaje,
                ', '.join(pizza.extras),
                pizza.tamaño,
                Precios('pizzas.csv').calcular_precio(pizza),
            ])

    def leer_pizzas(self):
        pizzas = []
        try:
            with open(self.file_path, mode='r', newline='', encoding="UTF-8") as file:
                reader = csv.reader(file)
                # Salta la primera fila (encabezados)
                next(reader)
                for row in reader:
                    # Asegurarse de que haya suficientes valores en la fila
                    if len(row) == 9:
                        masa, salsa, ingredientes_str, tecnica, presentacion, maridaje, extras, tamaño, precio = row
                        # Convierte la lista de ingredientes y extras a listas
                        ingredientes = ingredientes_str.split(', ')
                        extras = extras.split(', ')
                        # Convierte el precio a decimal
                        precio_decimal = Decimal(precio)
                        # Procesa cada fila y crea instancias de Pizza
                        pizza = Pizza(
                            masa,
                            salsa,
                            ingredientes,
                            tecnica,
                            presentacion,
                            maridaje,
                            extras,
                            tamaño,
                        )
                        pizza.precio = precio_decimal
                        pizzas.append(pizza)
        except FileNotFoundError:
            print("El archivo CSV no existe. Crea uno para almacenar las pizzas.")
        return pizzas

    def crear_precio(self, precio):
        with open(self.file_path, mode='a', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                precio.precio,
            ])

    def guardar_usuario(self, usuario):
        with open(self.file_path, mode='a', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                usuario.usuario,
                usuario.contraseña,
            ])

    def leer_usuarios(self):
        usuarios = []
        try:
            with open(self.file_path, mode='r', newline='', encoding="UTF-8") as file:
                reader = csv.reader(file)
                # Salta la primera fila (encabezados)
                next(reader)
                for row in reader:
                    # Asegurarse de que haya suficientes valores en la fila
                    if len(row) >= 2:
                        usuario, contraseña = row
                        # Procesa cada fila y crea instancias de Usuario
                        usuario = Usuario(
                            usuario,
                            contraseña,
                        )
                        usuarios.append(usuario)
        except FileNotFoundError:
            print("El archivo CSV no existe. Crea uno para almacenar los usuarios.")
        return usuarios

    def guardar_menu(self, menu):
        with open(self.file_path, mode='a', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file)
            menu_data = menu.to_dict()
            # Escribe los datos del menú en el archivo CSV
            writer.writerow([
                menu_data.get("nombre", ""),
                menu_data.get("precio", ""),
                menu_data.get("entrante", ""),
                menu_data.get("pizza", ""),
                menu_data.get("bebida", ""),
                menu_data.get("postre", ""),
                menu_data.get("descuento", "")
            ])

    def leer_menus(self):
        menus = []
        try:
            with open(self.file_path, mode='r', newline='', encoding="UTF-8") as file:
                reader = csv.reader(file)
                # Salta la primera fila (encabezados)
                next(reader)
                for row in reader:
                    # Asegurarse de que haya suficientes valores en la fila
                    if len(row) >= 6:
                        nombre, precio, entrante, pizza, bebida, postre = row
                        # Convertir precio a decimal
                        precio_decimal = Decimal(precio)
                        # Procesa cada fila y crea instancias de MenuComposite
                        menu = MenuComposite(
                            nombre=nombre,
                            precio=precio_decimal,
                            entrante=entrante,
                            pizza=pizza,
                            bebida=bebida,
                            postre=postre,
                        )
                        menus.append(menu)
        except FileNotFoundError:
            print("El archivo CSV no existe. Crea uno para almacenar los menús.")
        return menus
