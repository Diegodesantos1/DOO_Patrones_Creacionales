from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .forms import PizzaBuilderForm, UsuarioBuilderForm, LoginBuilderForm
from .models import Pizza, Usuario
from .storage import CSVStorage

# Create your views here.


def index(request):
    return render(request, "PizzeriaWebApp/index.html")


def menu(request):
    return render(request, "PizzeriaWebApp/menu.html")


def pizza(request):
    return render(request, "PizzeriaWebApp/pizza.html")


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

            # Cifrar la contraseña con las funciones de Django
            hashed_password = make_password(contraseña)

            usuario = Usuario(
                usuario=usuario,
                contraseña=hashed_password,
            )

            # Almacenar el usuario cifrado
            storage = CSVStorage('usuarios.csv')
            storage.guardar_usuario(usuario)

            return redirect('index')

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


def login(request):
    if request.method == 'POST':
        form = LoginBuilderForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificar si el usuario y la contraseña existen en el CSV
            storage = CSVStorage('usuarios.csv')
            usuarios = storage.leer_usuarios()
            for usuario in usuarios:
                if usuario.usuario == username and check_password(password, usuario.contraseña):
                    user = authenticate(
                        request, username=username, password=usuario.contraseña)
                    if user is not None:
                        login(request, user)
                        # Redirige a la página después del inicio de sesión
                        return redirect('pagina_despues_del_login')
                    else:
                        # Mostrar un mensaje de error si la autenticación falla
                        error_message = "Nombre de usuario o contraseña incorrecta."

            error_message = "Nombre de usuario o contraseña incorrecta."
    else:
        form = LoginBuilderForm()
        error_message = None

    return render(request, 'PizzeriaWebApp/login.html', {'form': form, 'error_message': error_message})
