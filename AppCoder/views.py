from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
# Create your views here.

def inicio(request):

      return render(request, "AppCoder/inicio.html")

def vegan(request):

      return render(request, "AppCoder/vegan.html")

def vegetarian(request):

      return render(request, "AppCoder/vegetarian.html")


def meats(request):

      return render(request, "AppCoder/meats.html")


def glutenFree(request):

      return render(request, "AppCoder/glutenFree.html")


def VeganFormulario(request):
      if request.method == "POST":
            miFormulario = VeganFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vegan = Vegan(nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  vegan.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = veganFormulario()
            
      return render(request, "AppCoder/veganFormulario.html", {"miFormulario": miFormulario})

def VegetarianFormulario(request):
      if request.method == "POST":
            miFormulario = VegetarianFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  Vegetarian = vegetarian(nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  Vegetarian.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = vegetarianFormulario()
            
      return render(request, "AppCoder/vegetarianFormulario.html", {"miFormulario": miFormulario})

def MeatsFormulario(request):
      if request.method == "POST":
            miFormulario = MeatsFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  meats = Meats (nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  meats.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = meatsFormulario()
            
      return render(request, "AppCoder/meatsFormulario.html", {"miFormulario": miFormulario})

def GlutenFreeFormulario(request):
      if request.method == "POST":
            miFormulario = GlutenFreeFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  glutenFree = glutenFree(nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  vegan.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = glutenFreeFormulario()
            
      return render(request, "AppCoder/glutenFreeFormulario.html", {"miFormulario": miFormulario})

def busquedaVegetariano(request):
      return render(request, "AppCoder/busquedaVegetariano.html")

def buscar(request):
      if request.GET["nombre"]:
            
            nombre = request.GET['nombre']
            
            Vegetarian = Vegetarian.objects.filter(nombre__icontains=nombre)
            
            return render(request, "AppCoder/resultadoBusqueda.html",{"nombre":nombre})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)