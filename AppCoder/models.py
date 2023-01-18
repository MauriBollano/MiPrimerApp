from django.db import models

# Create your models here.
class Vegan(models.Model):

    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)
    

class Meats(models.Model):
    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)

class Vegetarian(models.Model):
    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)

class glutenFree(models.Model):
    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)

