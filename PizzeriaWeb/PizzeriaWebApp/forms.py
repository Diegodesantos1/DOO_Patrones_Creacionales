
from django import forms

# importar los modelos
from .models import Pizza, Masa, Salsa, Ingredientes, Tecnica, Presentacion, Maridaje

class PizzaForm(forms.Form):
    masa = forms.ChoiceField(choices=Masa.masas_disponibles())
    salsa = forms.ChoiceField(choices=Salsa.salsas_disponibles())
    ingredientes = forms.MultipleChoiceField(choices=Ingredientes.ingredientes_disponibles())
    tecnica = forms.ChoiceField(choices=Tecnica.tecnicas_disponibles())
    presentacion = forms.ChoiceField(choices=Presentacion.presentaciones_disponibles())
    maridaje = forms.ChoiceField(choices=Maridaje.maridajes_disponibles())
    extras = forms.MultipleChoiceField(choices=Ingredientes.ingredientes_disponibles())