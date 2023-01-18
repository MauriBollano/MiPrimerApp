from django import forms

class veganFormulario(forms.Form):
    nombre =forms.CharField()
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()

class vegetarianFormulario(forms.Form):
    nombre =forms.CharField()
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()

class meatsFormulario(forms.Form):
    nombre =forms.CharField()
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()


class glutenFreeFormulario(forms.Form):
    nombre =forms.CharField()
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()
