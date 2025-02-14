from django.shortcuts import render, get_list_or_404
from .models import Post

def Lista_de_publicaciones(request):
    publicaciones = get_list_or_404(Post)
    publicaciones = Post.objects.all() 
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def Detalle_publicacion(request, titulo_arg, tema_arg):
    publicacion = get_list_or_404(Post, titulo=titulo_arg, tema=tema_arg)
    return render(request, 'post_unico.html', {'publicacion': publicacion})    
