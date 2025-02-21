from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post, Comentario
from django.views.generic import ListView
from .forms import Formulario_Envio_de_Correo, ComentarioFormulario
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post, Comentario
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from .forms import Formulario_Envio_de_Correo, ComentarioFormulario, SearchForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Lista_de_publicaciones(request, tag_slug=None):
    tag = None
    object_list = Post.objects.all()  # Inicializa object_list con todos los posts

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])  # Filtra solo si hay un tag

    paginacion = Paginator(object_list, 2)  # La paginación va después de la consulta
    pagina = request.GET.get('pagina')

    try:
        publicaciones = paginacion.page(pagina)
    except PageNotAnInteger:
        publicaciones = paginacion.page(1)
    except EmptyPage:
        publicaciones = paginacion.page(paginacion.num_pages)

    return render(request, 'lista_posts.html', {'publicaciones': publicaciones, 'tag': tag})


def Detalle_publicacion(request, titulo_arg, tema_arg):
    publicacion = get_object_or_404(Post, titulo=titulo_arg, tema=tema_arg)
    comentarios = publicacion.comments.filter(activo=True)
    nuevo_comentario = None

    # Se crea el formulario *antes* del condicional
    comentario_form = ComentarioFormulario()

    if request.method == 'POST':
        # Se *reemplaza* con los datos del POST si es necesario
        comentario_form = ComentarioFormulario(data=request.POST)

        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.publicacion = publicacion
            nuevo_comentario.save()
            # Si quieres, puedes crear un nuevo formulario vacío después de guardar el comentario
            comentario_form = ComentarioFormulario()  # Limpia el formulario para el siguiente comentario

    return render(request, 'post_unico.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'nuevo_comentario': nuevo_comentario,
        'comentario_form': comentario_form
    })
  
def Compartir_Post(request, post_id):
    
    publicacion = get_object_or_404(Post, id=post_id, estado='publicado')

    if request.method == 'POST':
        formulario = Formulario_Envio_de_Correo(request.POST)
        if formulario.is_valid():
            cd = formulario.cleaned_data
            # Enviar el correo
        else:
            formulario = Formulario_Envio_de_Correo()

        return render(request, 'compartir_post.html', {'publicacion': publicacion, 'form': formulario})
    
def busqueda_publicaciones(request):
    form = SearchForm()
    consulta = None
    resultados = []

    if 'consulta' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = Post.objects.annotate(similarity=TrigramSimilarity('titulo', consulta),).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request, 'busqueda.html', {'form': form, 'consulta': consulta, 'resultados': resultados})