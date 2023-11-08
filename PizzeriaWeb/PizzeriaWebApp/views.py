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

            # Verificar que las contraseñas coincidan
            if contraseña != confirmar_contraseña:
                return render(request, 'PizzeriaWebApp/registro.html', {'form': form, 'error_message': 'Las contraseñas no coinciden'})

            usuario = Usuario(
                usuario=usuario,
                contraseña=contraseña,
            )

            # Almacenar el usuario cifrado
            storage = CSVStorage('usuarios.csv')
            storage.guardar_usuario(usuario)

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
                extras=extras
            )

            storage = CSVStorage('pizzas.csv')
            storage.guardar_pizza(pizza)

            return redirect('index')

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
