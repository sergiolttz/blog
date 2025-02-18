from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('lista/', Lista_de_publicaciones, name='lista'),
    path('tag/<slug:tag_slug>/', Lista_de_publicaciones, name='lista_tags'),
    #path('<int:post_id>/compartir/', compartir_post, name='compartir'),
    path('<str:titulo_arg>/<str:tema_arg>/', Detalle_publicacion, name='detalles'),
]