from django.contrib import admin
from .models import * 

#importamos el archivo models
# Register your models here.
# registramos los modelos

admin.site.register(Vegan)

admin.site.register(Meats)

admin.site.register(Vegetarian)

admin.site.register(glutenFree)
