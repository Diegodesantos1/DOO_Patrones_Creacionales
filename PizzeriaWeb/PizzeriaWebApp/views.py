from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PizzaBuilderForm, UsuarioBuilderForm, LoginBuilderForm
from .models import Pizza, Usuario
from .storage import CSVStorage

# Create your views here.


def index(request):
    return render(request, "PizzeriaWebApp/index.html")


def menu(request):
    return render(request, "PizzeriaWebApp/menu.html")


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

            pizza = Pizza(
                masa=masa,
                salsa=salsa,
                ingredientes=ingredientes,
                tecnica=tecnica,
                presentacion=presentacion,
                maridaje=maridaje,
                extras=extras,
            )

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
