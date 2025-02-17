from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Lista_de_publicaciones(request):
    paginacion = Paginator(Post.objects.all(), 2)
    pagina = request.GET.get('pagina')

    try:
        publicaciones = paginacion.page(pagina)
    except PageNotAnInteger:
        publicaciones = paginacion.page(1) 
    except EmptyPage:
        publicaciones = paginacion.page(paginacion.num_pages)
    return render(request, 'lista_posts.html', {'publicaciones': publicaciones})

    '''
    publicaciones = get_list_or_404(Post)
    publicaciones = Post.objects.all() 
    return render(request, 'lista_posts.html', {'publicaciones': publicaciones})
    '''

def Detalle_publicacion(request, titulo_arg, tema_arg):
    publicacion = get_object_or_404(Post, titulo=titulo_arg, tema=tema_arg)
    return render(request, 'post_unico.html', {'publicacion': publicacion})  
  