from django.db import models

# Creo los modelos de mi App

class Juego(models.Model):

    nombre = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    jugadores = models.CharField(max_length=40)

class Influencer(models.Model):

    nombre = models.CharField(max_length=40)
    nacimiento = models.IntegerField()

class Plataforma(models.Model):

    nombre = models.CharField(max_length=40)
    ceo = models.CharField(max_length=40)