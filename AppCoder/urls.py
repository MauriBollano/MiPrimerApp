from django.urls import path

from AppCoder import views

urlpatterns = [
    
    path('', views.inicio, name= "Inicio"), #esta era nuestra primer view
    path('vegan', views.vegan, name="Vegan"),
    path('vegetarian', views.vegetarian, name="Vegetarian"),
    path('meats', views.meats, name="Meats"),
    path('glutenFree', views.glutenFree, name="Gluten Free"),
    path('veganFormulario', views.VeganFormulario, name="VeganFormulario"),
    path('vegetarianFormulario', views.VegetarianFormulario, name="VegetarianFormulario"),
    path('meatsFormulario', views.MeatsFormulario, name="MeatsFormulario"),
    path('glutenFreeFormulario', views.GlutenFreeFormulario, name="GlutenFreeFormulario"),
    path('busquedaVegetariano', views.busquedaVegetariano, name="BusquedaVegetariano"),
    path('resultadoBusqueda', views.buscar),
] 

