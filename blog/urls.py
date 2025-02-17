from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('lista/', Lista_de_publicaciones.as_view(), name='lista'),
    path('<str:titulo_arg>/<str:tema_arg>/', Detalle_publicacion, name='detalles'),
]