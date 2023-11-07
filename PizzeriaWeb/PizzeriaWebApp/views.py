from django.shortcuts import render, HttpResponse, redirect
from .forms import PizzaForm
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
        form = PizzaForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            masa = form.cleaned_data['masa']
            salsa = form.cleaned_data['salsa']
            ingredientes = form.cleaned_data['ingredientes']
            tecnica = form.cleaned_data['tecnica']
            presentacion = form.cleaned_data['presentacion']
            maridaje = form.cleaned_data['maridaje']
            extras = form.cleaned_data['extras']

            # Crear una instancia de Pizza
            pizza = Pizza(
                masa=masa,
                salsa=salsa,
                ingredientes=ingredientes,
                tecnica=tecnica,
                presentacion=presentacion,
                maridaje=maridaje,
                extras=extras
            )

            # Guardar la pizza en el archivo CSV
            storage = CSVStorage('pizzas.csv')
            storage.guardar_pizza(pizza)

            # Redirigir a la página de creación de pizza
            return redirect('pizza')

    else:
        form = PizzaForm()

    return render(request, 'PizzeriaWebApp/pizza.html', {'form': form})
