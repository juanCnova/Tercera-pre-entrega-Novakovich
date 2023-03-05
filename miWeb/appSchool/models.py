from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()
    legajo = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()
    profesion = models.CharField(max_length=15)

class Nota(models.Model):
    materia = models.CharField(max_length=15)
    alumno = models.CharField(max_length=30)
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

class Materia(models.Model):
    nombre = models.CharField(max_length=15)
    profesor = models.CharField(max_length=15)

