from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre