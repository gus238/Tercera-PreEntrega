from django import forms

class form_influencer_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    nacimiento = forms.IntegerField()

class form_juego_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    empresa = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)
    jugadores = forms.CharField(max_length=40)

class form_plataforma_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    ceo = forms.CharField(max_length=40)