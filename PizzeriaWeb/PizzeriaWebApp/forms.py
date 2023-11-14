from django import forms


class PizzaBuilderForm(forms.Form):
    MASA_CHOICES = [
        ('Delgada', 'Delgada'),
        ('Pan', 'Pan'),
        ('Fermentada', 'Fermentada'),
        ('Sin gluten', 'Sin gluten'),
        ('Integral', 'Integral'),
        ('Tradicional', 'Tradicional'),

    ]
    SALSA_CHOICES = [
        ('Tomate', 'Tomate'),
        ('Pesto', 'Pesto'),
        ('BBQ', 'BBQ'),
        ('Yogur', 'Yogur'),
        ('Carbonara', 'Carbonara'),
        ('Sin salsa', 'Sin salsa'),
    ]
    INGREDIENTES_CHOICES = [
        ('Jamón', 'Jamón'),
        ('Queso', 'Queso'),
        ('Champiñones', 'Champiñones'),
        ('Tomate', 'Tomate'),
        ('Pimiento', 'Pimiento'),
        ('Pepperoni', 'Pepperoni'),
        ('Albahaca', 'Albahaca'),
        ('Aceitunas', 'Aceitunas'),
        ('Carne Picada', 'Carne Picada'),
        ('Cebolla', 'Cebolla'),
    ]
    TECNICA_CHOICES = [
        ('Horno tradicional', 'Horno tradicional'),
        ('Cocina a la leña', 'Cocina a la leña'),
        ('Cocina molecular', 'Cocina molecular'),
        ('Asado', 'Asado'),
    ]
    PRESENTACION_CHOICES = [
        ('Clásica', 'Clásica'),
        ('Artística', 'Artística'),
        ('Personalizada', 'Personalizada'),
        ('Calzone', 'Calzone'),
    ]
    MARIDAJE_CHOICES = [
        ('Vino', 'Vino'),
        ('Cerveza', 'Cerveza'),
        ('Cóctel', 'Cóctel'),
        ('Refresco', 'Refresco'),
        ('Agua', 'Agua'),
        ('Café', 'Café'),
        ('Té', 'Té')
    ]

    EXTRAS_CHOICES = [
        ('Queso extra', 'Queso extra'),
        ('Salsa extra', 'Salsa extra'),
        ('Borde de queso', 'Borde de queso'),
        ('Aceite de oliva', 'Aceite de oliva'),
    ]

    TAMAÑOS_CHOICES = [
        ('Pequeña', 'Pequeña'),
        ('Mediana', 'Mediana'),
        ('Grande', 'Grande'),
        ('Familiar', 'Familiar'),
    ]

    masa = forms.ChoiceField(
        choices=[('', 'Seleccione una masa')] + MASA_CHOICES)
    salsa = forms.ChoiceField(
        choices=[('', 'Seleccione una salsa')] + SALSA_CHOICES)
    ingredientes = forms.MultipleChoiceField(
        choices=INGREDIENTES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    tecnica = forms.ChoiceField(
        choices=[('', 'Seleccione una técnica')] + TECNICA_CHOICES)
    presentacion = forms.ChoiceField(
        choices=[('', 'Seleccione una presentación')] + PRESENTACION_CHOICES)
    maridaje = forms.ChoiceField(
        choices=[('', 'Seleccione un maridaje')] + MARIDAJE_CHOICES,
    )
    extras = forms.MultipleChoiceField(
        choices=EXTRAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    tamaño = forms.ChoiceField(
        choices=[('', 'Seleccione un tamaño')] + TAMAÑOS_CHOICES,
    )


class UsuarioBuilderForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput, max_length=100)
    confirmar_contraseña = forms.CharField(
        widget=forms.PasswordInput, label='Confirmar Contraseña')


class LoginBuilderForm(forms.Form):
    usuario = forms.CharField(max_length=100, label="Nombre de usuario")
    contraseña = forms.CharField(
        widget=forms.PasswordInput, label="Contraseña")


class MenuCompositeForm(forms.Form):
    ENTRANTE_CHOICES = [
        ('Ensalada', 'Ensalada'),
        ('Sopa', 'Sopa'),
        ('Pan', 'Pan'),
        ('Patatas', 'Patatas'),
        ('Croquetas', 'Croquetas'),
        ('Empanadillas', 'Empanadillas'),
    ]
    PIZZAS_CHOICES = [
        ('Barbacoa', 'Barbacoa'),
        ('Carbonara', 'Carbonara'),
        ('Cuatro quesos', 'Cuatro quesos'),
        ('Cuatro estaciones', 'Cuatro estaciones'),
        ('Diávola', 'Diávola'),
        ('Hawaiana', 'Hawaiana'),
        ('Margarita', 'Margarita'),
        ('Funghi', 'Funghi'),
        ('Vegetariana', 'Vegetariana'),
    ]
    BEBIDAS_CHOICES = [
        ('Vino', 'Vino'),
        ('Cerveza', 'Cerveza'),
        ('Cóctel', 'Cóctel'),
        ('Refresco', 'Refresco'),
        ('Agua', 'Agua'),
        ('Café', 'Café'),
        ('Té', 'Té')
    ]

    POSTRES_CHOICES = [
        ('Tarta de queso', 'Tarta de queso'),
        ('Tarta de chocolate', 'Tarta de chocolate'),
        ('Flan', 'Flan'),
        ('Helado', 'Helado'),
        ('Fruta', 'Fruta'),
        ('Yogur', 'Yogur'),
    ]

    DESCUENTOS_CHOICES=[
        ('5% de descuento', '5% de descuento'),
        ('10% de descuento', '10% de descuento'),
        ('15% de descuento', '15% de descuento'),
    ]
    entrante = forms.ChoiceField(
        choices=[('', 'Seleccione un entrante')] + ENTRANTE_CHOICES)
    pizza = forms.ChoiceField(
        choices=[('', 'Seleccione una pizza')] + PIZZAS_CHOICES)
    bebida = forms.ChoiceField(
        choices=[('', 'Seleccione una bebida')] + BEBIDAS_CHOICES)

    postre = forms.ChoiceField(
        choices=[('', 'Seleccione un postre')] + POSTRES_CHOICES)
    
    descuento = forms.ChoiceField(
        choices=[('', 'Seleccione un descuento')] + DESCUENTOS_CHOICES)
