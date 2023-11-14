from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import PizzaBuilderForm, UsuarioBuilderForm, LoginBuilderForm, MenuCompositeForm
from .models import Pizza, Usuario, MenuInfantil, Bebida, Postre, Entrante, Pizza_Menu, ComponenteMenu
from .storage import CSVStorage
from .price import Precios
from decimal import Decimal

# Create your views here.


def index(request):
    return render(request, "PizzeriaWebApp/index.html")


def menu(request):
    return render(request, "PizzeriaWebApp/menu.html")


def menu_pedidos(request):
    storage = CSVStorage('menus.csv')
    menus = storage.leer_menus()

    # Asegúrate de que haya al menos un menú en la lista
    if menus:
        menu = menus[-1]
        return render(request, "PizzeriaWebApp/menu_pedidos.html", {'menu': menu})
    else:
        return render(request, "PizzeriaWebApp/menu_pedidos.html", {'menu': None})


def menuinfantil(request):
    if request.method == 'POST':
        form = MenuCompositeForm(request.POST)
        if form.is_valid():
            entrante = form.cleaned_data['entrante']
            pizza = form.cleaned_data['pizza']
            bebida = form.cleaned_data['bebida']
            postre = form.cleaned_data['postre']
            descuento = form.cleaned_data['descuento']

            # Define un diccionario para mapear descuentos a porcentajes
            descuento_porcentajes = {
                '5% de descuento': 0.05,
                '10% de descuento': 0.10,
                '15% de descuento': 0.15,
            }

            # Calcula el precio base del menú infantil
            precio_base = 7.50

            # Calcula el porcentaje de descuento
            porcentaje_descuento = descuento_porcentajes[descuento]

            # Calcula el precio con descuento
            precio_descuento = precio_base - \
                (precio_base * porcentaje_descuento)

            menu_infantil = MenuInfantil(
                entrante=entrante,
                pizza=pizza,
                bebida=bebida,
                postre=postre,
                descuento=descuento,
            )

            menu_infantil.precio = precio_descuento
            menu_infantil.nombre = "Menu Infantil"
            storage = CSVStorage('menus.csv')
            storage.guardar_menu(menu_infantil)

            return render(request, 'PizzeriaWebApp/menu_pedidos.html', {'menu': menu_infantil})
    else:
        form = MenuCompositeForm()

    return render(request, 'PizzeriaWebApp/menuinfantil.html', {'form': form})


def menudoble(request):
    return render(request, "PizzeriaWebApp/menudoble.html")


def menutriple(request):
    return render(request, "PizzeriaWebApp/menutriple.html")


def menufamiliar(request):
    return render(request, "PizzeriaWebApp/menufamiliar.html")


def registro(request):
    if request.method == 'POST':
        form = UsuarioBuilderForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            confirmar_contraseña = form.cleaned_data['confirmar_contraseña']

            # Verificar que el usuario no exista
            storage = CSVStorage('usuarios.csv')
            lista_usuarios = storage.leer_usuarios()
            usuario_existe = False

            for usuario_actual in lista_usuarios:
                if usuario_actual.usuario == usuario:
                    usuario_existe = True
                    break

            if usuario_existe == True:
                messages.error(
                    request, 'El nombre de usuario ya existe, por favor elige otro.')

            else:

                # Verificar que las contraseñas coincidan
                if contraseña != confirmar_contraseña:
                    messages.error(request, 'Las contraseñas no coinciden')

                    return redirect('registro')
                else:
                    usuario = Usuario(
                        usuario=usuario,
                        contraseña=contraseña,
                    )

                    # Almacenar el usuario cifrado
                    storage = CSVStorage('usuarios.csv')
                    storage.guardar_usuario(usuario)

                    messages.success(
                        request, 'Registro exitoso. Ahora puedes iniciar sesión.')

                return redirect('login')

    else:
        form = UsuarioBuilderForm()

    return render(request, 'PizzeriaWebApp/registro.html', {'form': form})


def pizza(request):
    if request.method == 'POST':
        form = PizzaBuilderForm(request.POST)
        if form.is_valid():
            masa = form.cleaned_data['masa']
            salsa = form.cleaned_data['salsa']
            ingredientes = form.cleaned_data['ingredientes']
            tecnica = form.cleaned_data['tecnica']
            presentacion = form.cleaned_data['presentacion']
            maridaje = form.cleaned_data['maridaje']
            extras = form.cleaned_data['extras']
            tamaño = form.cleaned_data['tamaño']

            pizza = Pizza(
                masa=masa,
                salsa=salsa,
                ingredientes=ingredientes,
                tecnica=tecnica,
                presentacion=presentacion,
                maridaje=maridaje,
                extras=extras,
                tamaño=tamaño,
            )

            # Calcular el precio
            precio_calculado = Precios('pizzas.csv').calcular_precio(pizza)
            pizza.precio = precio_calculado

            # Guardar la pizza
            storage = CSVStorage('pizzas.csv')
            storage.guardar_pizza(pizza)

            return redirect('pedidos')

    else:
        form = PizzaBuilderForm()

    return render(request, 'PizzeriaWebApp/pizza.html', {'form': form})


def datos(request):
    # Cargar los datos del archivo CSV
    storage = CSVStorage('pizzas.csv')
    pizzas = storage.leer_pizzas()

    return render(request, 'PizzeriaWebApp/datos.html', {'pizzas': pizzas})


def datos_usuarios(request):
    datos = CSVStorage('usuarios.csv')
    usuarios = datos.leer_usuarios()

    return render(request, 'PizzeriaWebApp/datos_usuarios.html', {'usuarios': usuarios})


def login(request):
    if request.method == 'POST':
        form = LoginBuilderForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']

            # Verificar que el usuario exista
            storage = CSVStorage('usuarios.csv')
            usuarios = storage.leer_usuarios()
            usuario_correcto = None

            for usuario_actual in usuarios:
                if usuario_actual.usuario == usuario and usuario_actual.contraseña == contraseña:
                    usuario_correcto = usuario_actual.usuario
                    break

            if usuario_correcto:
                # Almacena el nombre de usuario en la sesión
                request.session['username'] = usuario_correcto
                return redirect('index')

            else:
                messages.error(
                    request, 'Nombre de usuario o contraseña incorrectos')
                return render(request, 'PizzeriaWebApp/login.html', {'form': form})

    else:
        form = LoginBuilderForm()

    return render(request, 'PizzeriaWebApp/login.html', {'form': form})


def pedidos(request):
    # Cargar los datos del archivo CSV
    storage = CSVStorage('pizzas.csv')
    pizzas = storage.leer_pizzas()

    # toma la última pizza
    pizza = pizzas[-1]

    return render(request, 'PizzeriaWebApp/pedidos.html', {'pizza': pizza})


def recomendaciones(request):
    # Leer los datos de las pizzas desde el CSV
    storage = CSVStorage('pizzas.csv')
    pizzas = storage.leer_pizzas()

    # Procesar las pizzas y calcular ingredientes populares
    ingredientes_populares = {}
    for pizza in pizzas:
        for ingrediente in pizza.ingredientes:
            if ingrediente in ingredientes_populares:
                ingredientes_populares[ingrediente] += 1
            else:
                ingredientes_populares[ingrediente] = 1

    # Encontrar los ingredientes más populares
    ingredientes_recomendados = [ingrediente for ingrediente, count in sorted(
        ingredientes_populares.items(), key=lambda item: item[1], reverse=True)][:3]

    # Generar recomendaciones de pizzas basadas en los ingredientes populares
    recomendaciones_pizzas = []
    for pizza in pizzas:
        for ingrediente in pizza.ingredientes:
            if ingrediente in ingredientes_recomendados:
                recomendaciones_pizzas.append(pizza)
                break  # solo una vez por pizza

    return render(request, 'PizzeriaWebApp/recomendaciones.html', {'recomendaciones': recomendaciones_pizzas})
