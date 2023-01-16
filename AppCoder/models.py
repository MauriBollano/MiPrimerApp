from django.db import models

# Create your models here.
class Vegan(models.Model):

    nombre =models.CharField("Name",max_length=40)
    dificultad = models.CharField("Difficulty",max_length=10)
    tiempo = models.IntegerField("Time")
    calorias=models.IntegerField("Calories")
    receta=models.TextField("Recipes")
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    

class Meats(models.Model):
    nombre =models.CharField("Name",max_length=40)
    dificultad = models.CharField("Difficulty",max_length=10)
    tiempo = models.IntegerField("Time")
    calorias=models.IntegerField("Calories")
    receta=models.TextField("Recipes")
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")

class Vegetarian(models.Model):
    nombre =models.CharField("Name",max_length=40)
    dificultad = models.CharField("Difficulty",max_length=10)
    tiempo = models.IntegerField("Time")
    calorias=models.IntegerField("Calories")
    receta=models.TextField("Recipes")
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")

class glutenFree(models.Model):
    nombre =models.CharField("Name",max_length=40)
    dificultad = models.CharField("Difficulty",max_length=10)
    tiempo = models.IntegerField("Time")
    calorias=models.IntegerField("Calories")
    receta=models.TextField("Recipes")
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
