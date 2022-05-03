from django import forms
from django.core import validators
    
class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Título",
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Mete el título',
                'class': 'titulo_form_article'
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-záéíóúÁÉÍÓÚ0-9ñ ]*$', 'El título está mal formado', 'invalid_title')

        ]
    )

    #content = forms.CharField(
    #    label = "Contenido",
    #    widget = forms.Textarea(
    #        attrs = {
    #            'placeholder': 'Mete el contenido',
    #            'class': 'contenido_form_article'
    #        }
    #    ),
    #)

    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        validators = [
            validators.MaxLengthValidator(50, 'Te has pasado con mucho texto!')
        ]
    )

    content.widget.attrs.update({
        'placeholder': 'Mete el contenido',
        'class': 'contenido_form_article' 
    })

    public_options = [
        (0, 'No'),
        (1, 'Si')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado",
        choices = public_options
    )