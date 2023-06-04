from django.db import models




# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"nombre: {self.nombre}, apellido {self.apellido}, edad {self.edad}"
    