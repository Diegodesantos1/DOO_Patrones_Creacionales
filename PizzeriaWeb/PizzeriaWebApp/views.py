from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import PizzaBuilderForm
from .models import Pizza
from .storage import CSVStorage

# Create your views here.

def index(request):
    return render(request, "PizzeriaWebApp/index.html")


def menu(request):
    return render(request, "PizzeriaWebApp/menu.html")


def pizza(request):
    return render(request, "PizzeriaWebApp/pizza.html")


def registro(request):
    return render(request, "PizzeriaWebApp/registro.html")


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

def registro(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validar que las contraseñas coincidan
        if password == confirm_password:
            # Cifrar la contraseña
            hashed_password = make_password(password)

            # Guardar el usuario y la contraseña cifrada en un archivo CSV
            with open('usuarios.csv', 'a', newline='') as csvfile:
                next(reader)
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([username, hashed_password])

            return redirect('login')  # Redirigir a la página de inicio de sesión
        else:
            # Las contraseñas no coinciden, manejar el error apropiadamente
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})
    else:
        return render(request, 'registro.html')
