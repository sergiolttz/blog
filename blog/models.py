from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

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
    