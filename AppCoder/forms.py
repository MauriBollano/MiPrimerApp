from django import forms

class veganFormulario(forms.Form):
    nombre =forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()
    calorias=forms.IntegerField()
    imagen = forms.ImageField()

class vegetarianFormulario(forms.Form):
    nombre =forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()
    calorias=forms.IntegerField()
    imagen = forms.ImageField()

class meatsFormulario(forms.Form):
    nombre =forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()
    calorias=forms.IntegerField()
    imagen = forms.ImageField()

class glutenFreeFormulario(forms.Form):
    nombre =forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()
    calorias=forms.IntegerField()
    imagen = forms.ImageField()