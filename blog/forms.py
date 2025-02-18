from django import forms

class Formulario_Envio_de_Correo(forms.form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    destinatario = forms.EmailField()
    comentarios = forms.CharField(widget=forms.Textarea, required=False)