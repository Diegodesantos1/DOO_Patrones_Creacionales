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


class MenuCompositeIndividualForm(forms.Form):
    ENTRANTE_CHOICES = [
        ('Ensalada', 'Ensalada'),
        ('Pan', 'Pan'),
        ('Patatas fritas', 'Patatas fritas'),
        ('Croquetas', 'Croquetas'),
        ('Empanadillas', 'Empanadillas'),
        ('Nuggets', 'Nuggets'),
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

    DESCUENTOS_CHOICES = [
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


class MenuCompositeInfantilForm(forms.Form):
    ENTRANTE_CHOICES = [
        ('Ensalada', 'Ensalada'),
        ('Pan', 'Pan'),
        ('Patatas fritas', 'Patatas fritas'),
        ('Croquetas', 'Croquetas'),
        ('Empanadillas', 'Empanadillas'),
        ('Nuggets', 'Nuggets'),
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
        ('Refresco', 'Refresco'),
        ('Agua', 'Agua'),
        ('Zumo', 'Zumo'),
    ]

    POSTRES_CHOICES = [
        ('Tarta de queso', 'Tarta de queso'),
        ('Tarta de chocolate', 'Tarta de chocolate'),
        ('Flan', 'Flan'),
        ('Helado', 'Helado'),
        ('Fruta', 'Fruta'),
        ('Yogur', 'Yogur'),
    ]

    DESCUENTOS_CHOICES = [
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


class MenuCompositeDobleForm(forms.Form):
    ENTRANTES_CHOICES = [
        ('Ensalada', 'Ensalada'),
        ('Pan', 'Pan'),
        ('Patatas fritas', 'Patatas fritas'),
        ('Croquetas', 'Croquetas'),
        ('Empanadillas', 'Empanadillas'),
        ('Nuggets', 'Nuggets'),
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

    DESCUENTOS_CHOICES = [
        ('5% de descuento', '5% de descuento'),
        ('10% de descuento', '10% de descuento'),
        ('15% de descuento', '15% de descuento'),
    ]
    entrantes = forms.MultipleChoiceField(
        choices=ENTRANTES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    pizzas = forms.MultipleChoiceField(
        choices=PIZZAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    bebidas = forms.MultipleChoiceField(
        choices=BEBIDAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    postres = forms.MultipleChoiceField(
        choices=POSTRES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    descuento = forms.ChoiceField(
        choices=[('', 'Seleccione un descuento')] + DESCUENTOS_CHOICES
    )

    def clean(self):
        cleaned_data = super().clean()
        entrantes = cleaned_data.get('entrantes')
        pizzas = cleaned_data.get('pizzas')
        bebidas = cleaned_data.get('bebidas')
        postres = cleaned_data.get('postres')

        if not entrantes or not pizzas or not bebidas or not postres:
            raise forms.ValidationError(
                "Debe seleccionar 2 opciones en cada campo.")

        if (
            len(entrantes) != 2 or
            len(pizzas) != 2 or
            len(bebidas) != 2 or
            len(postres) != 2
        ):
            raise forms.ValidationError(
                "Debe seleccionar 2 opciones en cada campo.")


class MenuCompositeTripleForm(forms.Form):
    ENTRANTES_CHOICES = [
        ('Ensalada', 'Ensalada'),
        ('Pan', 'Pan'),
        ('Patatas fritas', 'Patatas fritas'),
        ('Croquetas', 'Croquetas'),
        ('Empanadillas', 'Empanadillas'),
        ('Nuggets', 'Nuggets'),
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

    DESCUENTOS_CHOICES = [
        ('5% de descuento', '5% de descuento'),
        ('10% de descuento', '10% de descuento'),
        ('15% de descuento', '15% de descuento'),
    ]
    entrantes = forms.MultipleChoiceField(
        choices=ENTRANTES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    pizzas = forms.MultipleChoiceField(
        choices=PIZZAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    bebidas = forms.MultipleChoiceField(
        choices=BEBIDAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    postres = forms.MultipleChoiceField(
        choices=POSTRES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    descuento = forms.ChoiceField(
        choices=[('', 'Seleccione un descuento')] + DESCUENTOS_CHOICES
    )

    def clean(self):
        cleaned_data = super().clean()
        entrantes = cleaned_data.get('entrantes')
        pizzas = cleaned_data.get('pizzas')
        bebidas = cleaned_data.get('bebidas')
        postres = cleaned_data.get('postres')

        if (
            len(entrantes) != 3 or
            len(pizzas) != 3 or
            len(bebidas) != 3 or
            len(postres) != 3
        ):
            raise forms.ValidationError(
                "Debe seleccionar exactamente 3 opciones en cada campo.")


class MenuCompositeFamiliarForm(forms.Form):
    ENTRANTES_CHOICES = [
        ('Ensalada', 'Ensalada'),
        ('Pan', 'Pan'),
        ('Patatas fritas', 'Patatas fritas'),
        ('Croquetas', 'Croquetas'),
        ('Empanadillas', 'Empanadillas'),
        ('Nuggets', 'Nuggets'),
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

    DESCUENTOS_CHOICES = [
        ('5% de descuento', '5% de descuento'),
        ('10% de descuento', '10% de descuento'),
        ('15% de descuento', '15% de descuento'),
    ]
    entrantes = forms.MultipleChoiceField(
        choices=ENTRANTES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    pizzas = forms.MultipleChoiceField(
        choices=PIZZAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    bebidas = forms.MultipleChoiceField(
        choices=BEBIDAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    postres = forms.MultipleChoiceField(
        choices=POSTRES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    descuento = forms.ChoiceField(
        choices=[('', 'Seleccione un descuento')] + DESCUENTOS_CHOICES
    )

    def clean(self):
        cleaned_data = super().clean()
        entrantes = cleaned_data.get('entrantes')
        pizzas = cleaned_data.get('pizzas')
        bebidas = cleaned_data.get('bebidas')
        postres = cleaned_data.get('postres')

        if (
            len(entrantes) != 4 or
            len(pizzas) != 4 or
            len(bebidas) != 4 or
            len(postres) != 4
        ):
            raise forms.ValidationError(
                "Debe seleccionar exactamente 4 opciones en cada campo.")
