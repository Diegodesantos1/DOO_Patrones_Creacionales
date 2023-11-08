# storage.py

from .models import Pizza, Usuario

import csv


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
                ', '.join(pizza.extras)
            ])

    def leer_pizzas(self):
        pizzas = []
        try:
            with open(self.file_path, mode='r', newline='', encoding="UTF-8") as file:
                reader = csv.reader(file)
                # Salta la primera fila (encabezados)
                next(reader)
                for row in reader:
                    # Procesa cada fila y crea instancias de Pizza
                    masa, salsa, ingredientes, tecnica, presentacion, maridaje, extras = row
                    ingredientes = [ingrediente.strip()
                                    for ingrediente in ingredientes.split(', ')]
                    extras = [extra.strip() for extra in extras.split(', ')]
                    pizza = Pizza(
                        masa,
                        salsa,
                        ingredientes,
                        tecnica,
                        presentacion,
                        maridaje,
                        extras
                    )
                    pizzas.append(pizza)
        except FileNotFoundError:
            print("El archivo CSV no existe. Crea uno para almacenar las pizzas.")
        return pizzas

    def guardar_usuario(self, usuario):
        with open(self.file_path, mode='a', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                usuario.usuario,
                usuario.contraseña,
            ])

            file.write('\n')

    def leer_usuarios(self):
        usuarios = []
        try:
            with open(self.file_path, mode='r', newline='', encoding="UTF-8") as file:
                reader = csv.reader(file)
                # Salta la primera fila (encabezados)
                next(reader)
                for row in reader:
                    # Procesa cada fila y crea instancias de Usuario
                    usuario, contraseña = row
                    usuario = Usuario(
                        usuario,
                        contraseña,
                    )
                    usuarios.append(usuario)
        except FileNotFoundError:
            print("El archivo CSV no existe. Crea uno para almacenar los usuarios.")
        return usuarios
