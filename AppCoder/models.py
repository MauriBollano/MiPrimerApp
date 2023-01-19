from django.db import models

# Create your models here.
class Vegan(models.Model):

    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Dificultad {self.dificultad} - Tiempo: {self.tiempo}"  

class Meats(models.Model):
    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)

    def __str__(self):
        return f"Nombre: {self.nombre} - Dificultad {self.dificultad} - Tiempo: {self.tiempo}"  

class Vegetarian(models.Model):
    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)

    def __str__(self):
        return f"Nombre: {self.nombre} - Dificultad {self.dificultad} - Tiempo: {self.tiempo}"

class GlutenFree(models.Model):
    nombre =models.CharField("nombre",max_length=40)
    dificultad = models.CharField("dificultad",max_length=10)
    tiempo = models.IntegerField("tiempo")
    receta=models.CharField("receta",max_length=600)

    def __str__(self):
        return f"Nombre: {self.nombre} - Dificultad {self.dificultad} - Tiempo: {self.tiempo}"

