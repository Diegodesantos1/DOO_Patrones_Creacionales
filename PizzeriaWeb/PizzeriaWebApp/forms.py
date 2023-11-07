
from django import forms

class PizzaForm(forms.Form):
    masa = forms.ChoiceField(choices=[('Delgada', 'Delgada'), ('Pan', 'Pan'), ('Fermentada', 'Fermentada')])
    salsa = forms.ChoiceField(choices=[('Tomate', 'Tomate'), ('Pesto', 'Pesto'), ('BBQ', 'BBQ')])
    ingredientes = forms.CharField(max_length=255)
    tecnica = forms.ChoiceField(choices=[('Horno tradicional', 'Horno tradicional'), ('Cocina a la leña', 'Cocina a la leña'), ('Cocina molecular', 'Cocina molecular')])
    presentacion = forms.ChoiceField(choices=[('Clásica', 'Clásica'), ('Artística', 'Artística'), ('Personalizada', 'Personalizada')])
    maridaje = forms.ChoiceField(choices=[('Vino', 'Vino'), ('Cerveza', 'Cerveza'), ('Coctel', 'Coctel')])
    extras = forms.CharField(max_length=255)
