import tkinter as tk
from Pizzeria.models import Pizza
from Pizzeria.builder import PizzaBuilder
from Pizzeria.storage import CSVStorage

def guardar_pizza():
    masa = masa_var.get()
    salsa = salsa_var.get()
    ingredientes = ingredientes_entry.get().split(', ')
    tecnica_coccion = tecnica_var.get()
    presentacion = presentacion_var.get()
    maridaje = maridaje_var.get()
    extras = extras_entry.get().split(', ')

    # Crear una nueva pizza utilizando el PizzaBuilder
    pizza_builder = PizzaBuilder()
    pizza_builder.select_masa(masa)
    pizza_builder.select_salsa(salsa)
    for ingrediente in ingredientes:
        pizza_builder.add_ingrediente(ingrediente)
    pizza_builder.select_tecnica_coccion(tecnica_coccion)
    pizza_builder.select_presentacion(presentacion)
    pizza_builder.select_maridaje(maridaje)
    for extra in extras:
        pizza_builder.add_extra(extra)
    pizza_personalizada = pizza_builder.build()

    # Guardar la pizza en el archivo CSV
    storage.guardar_pizza(pizza_personalizada)

    resultado_label.config(text="¡Pizza guardada!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Delizioso - Crea tu pizza personalizada")

# Crear variables para los campos de entrada
masa_var = tk.StringVar()
salsa_var = tk.StringVar()
tecnica_var = tk.StringVar()
presentacion_var = tk.StringVar()
maridaje_var = tk.StringVar()

# Crear campos de entrada y etiquetas
masa_label = tk.Label(ventana, text="Elige el tipo de masa (Delgada, Pan, Fermentada):")
masa_entry = tk.Entry(ventana, textvariable=masa_var)
salsa_label = tk.Label(ventana, text="Elige la salsa base (Tomate, Pesto, BBQ):")
salsa_entry = tk.Entry(ventana, textvariable=salsa_var)
ingredientes_label = tk.Label(ventana, text="Añade ingredientes a tu pizza (separados por comas):")
ingredientes_entry = tk.Entry(ventana)
tecnica_label = tk.Label(ventana, text="Elige la técnica de cocción (Horno tradicional, Cocina a la leña, Cocina molecular):")
tecnica_entry = tk.Entry(ventana, textvariable=tecnica_var)
presentacion_label = tk.Label(ventana, text="Elige la presentación de la pizza (Clásica, Artística, Personalizada):")
presentacion_entry = tk.Entry(ventana, textvariable=presentacion_var)
maridaje_label = tk.Label(ventana, text="Elige el maridaje (Vino, Cerveza, Coctel):")
maridaje_entry = tk.Entry(ventana, textvariable=maridaje_var)
extras_label = tk.Label(ventana, text="Añade extras a tu pizza (separados por comas):")
extras_entry = tk.Entry(ventana)

# Botón para guardar la pizza
guardar_button = tk.Button(ventana, text="Guardar Pizza", command=guardar_pizza)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")

# Colocar elementos en la ventana
masa_label.pack()
masa_entry.pack()
salsa_label.pack()
salsa_entry.pack()
ingredientes_label.pack()
ingredientes_entry.pack()
tecnica_label.pack()
tecnica_entry.pack()
presentacion_label.pack()
presentacion_entry.pack()
maridaje_label.pack()
maridaje_entry.pack()
extras_label.pack()
extras_entry.pack()
guardar_button.pack()
resultado_label.pack()

# Inicializar el objeto de almacenamiento CSV
storage = CSVStorage('pizzas.csv')

def main():
    # Iniciar la ventana
    ventana.mainloop()
