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


def veganFormulario(request):
      if request.method == "POST":
            miFormulario = VeganFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vegan = Vegan(nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  vegan.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = VeganFormulario()
            
      return render(request, "AppCoder/veganFormulario.html", {"miFormulario": miFormulario})

def vegetarianFormulario(request):
      if request.method == "POST":
            miFormulario = VegetarianFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  vegetarian = Vegetarian(nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  vegetarian.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = VegetarianFormulario()
            
      return render(request, "AppCoder/vegetarianFormulario.html", {"miFormulario": miFormulario})

def meatsFormulario(request):
      if request.method == "POST":
            miFormulario = MeatsFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  meats = Meats (nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  meats.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = MeatsFormulario()
            
      return render(request, "AppCoder/meatsFormulario.html", {"miFormulario": miFormulario})

def glutenFreeFormulario(request):
      if request.method == "POST":
            miFormulario = GlutenFreeFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  glutenFree = GlutenFree(nombre=informacion["nombre"], dificultad=informacion["dificultad"], tiempo=informacion["tiempo"],receta=informacion["receta"])
                  glutenFree.save()
                  return render(request, "AppCoder/inicio.html") 
      else:
            miFormulario = GlutenFreeFormulario()
            
      return render(request, "AppCoder/glutenFreeFormulario.html", {"miFormulario": miFormulario})


def busquedaVegetariano(request):
      return render(request, "AppCoder/busquedaVegetariano.html")

def buscarVegetariano(request):
      if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            if len(nombre)>25:
                  respuesta="Nombre demasiado largo"
            else:
                  nombrevege = request.GET['nombre']
                  rec=Vegetarian.objects.filter(nombre__icontains= nombrevege)
            
                  return render(request, "AppCoder/resultadoVegetariano.html",{"rec":rec, "query":nombrevege})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)


def busquedaVegano(request):
      return render(request, "AppCoder/busquedaVegano.html")

def buscarVegano(request):
      if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            if len(nombre)>25:
                  respuesta="Nombre demasiado largo"
            else:
                  nombrevegan = request.GET['nombre']
                  rec=Vegan.objects.filter(nombre__icontains= nombrevegan)
            
                  return render(request, "AppCoder/resultadoVegano.html",{"rec":rec, "query":nombrevegan})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)

def busquedaMeats(request):
      return render(request, "AppCoder/busquedaMeats.html")

def buscarMeats(request):
      if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            if len(nombre)>25:
                  respuesta="Nombre demasiado largo"
            else:
                  nombreMeats = request.GET['nombre']
                  rec=Meats.objects.filter(nombre__icontains= nombreMeats)
            
                  return render(request, "AppCoder/resultadoMeats.html",{"rec":rec, "query":nombreMeats})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)

def busquedaGlutenFree(request):
      return render(request, "AppCoder/busquedaGlutenFree.html")

def buscarGlutenFree(request):
      if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            if len(nombre)>25:
                  respuesta="Nombre demasiado largo"
            else:
                  nombreGlutenFree = request.GET['nombre']
                  rec=GlutenFree.objects.filter(nombre__icontains= nombreGlutenFree)
            
                  return render(request, "AppCoder/resultadoGlutenFree.html",{"rec":rec, "query":nombreGlutenFree})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)