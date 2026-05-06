from django.db import models

class Vacante(models.Model):
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
