# Register your models here.
from django.contrib import admin

from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'autor', 'estado')
    search_fields = ('titulo', 'cuerpo')
    ordering = ('estado', 'publicado')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'publicacion', 'creado')
    list_filter = ('activo', 'creado', 'actualizado')
    search_fields = ('nombre', 'correo', 'cuerpo')