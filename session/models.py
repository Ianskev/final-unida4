from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proyecto(models.Model):
    foto=models.URLField()
    titulo_proyecto=models.CharField(max_length=200)
    descripcion=models.TextField()
    tags=models.TextField()
    url_github=models.URLField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'proyectos'
    
    def __str__(self):
        return self.titulo_proyecto
