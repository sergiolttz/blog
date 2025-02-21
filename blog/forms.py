from django import forms
from .models import Comentario

class Formulario_Envio_de_Correo(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    destinatario = forms.EmailField()
    comentarios = forms.CharField(widget=forms.Textarea, required=False)

class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'correo', 'cuerpo')

class SearchForm(forms.Form):
    consulta = forms.CharField(max_length=100)