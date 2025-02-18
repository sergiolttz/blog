from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=250)
    tema = models.CharField(max_length=250, unique_for_date='publicado')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()

    publicado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrador')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def obtener_url_absoluto(self):
        return reverse('blog:detalles', args=[self.titulo, self.tema])
    
    tags = TaggableManager()
    
class Comentario(models.Model):
    publicacion = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    nombre = models.CharField(max_length=80)
    correo = models.EmailField()
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ('creado',)

    def __str__(self):
        return f'Comentario de {self.nombre} en {self.publicacion}'
    
