# Register your models here.
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'autor', 'estado')
    search_fields = ('titulo', 'cuerpo')
    ordering = ('estado', 'publicado')