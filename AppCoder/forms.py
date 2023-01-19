from django import forms

class VeganFormulario(forms.Form):
    nombre =forms.CharField()
    """ Deberia agregar que la receta se vea mas grande(solo con size no alcanza) """
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()

class VegetarianFormulario(forms.Form):
    nombre =forms.CharField()
    """ Deberia agregar que la receta se vea mas grande(solo con size no alcanza) """
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()

class MeatsFormulario(forms.Form):
    nombre =forms.CharField()
    """ Deberia agregar que la receta se vea mas grande(solo con size no alcanza) """
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()


class GlutenFreeFormulario(forms.Form):
    nombre =forms.CharField()
    """ Deberia agregar que la receta se vea mas grande(solo con size no alcanza) """
    receta= forms.CharField()
    dificultad =forms.CharField()
    tiempo =forms.IntegerField()
