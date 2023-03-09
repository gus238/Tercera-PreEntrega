from django.urls import path
from AppGenerica import views

# Creo mis urls

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('crear_juego/', views.juego_formulario, name='Juegos'),
    path('buscar_juego/', views.buscar_juego, name='BuscarJuego'),
    path('resultado_juego/', views.resultado_juego),
    path('crear_influencer/', views.influencer_formulario, name='Influencers'),
    path('buscar_influencer/', views.buscar_influencer, name='BuscarInfluencer'),
    path('resultado_influencer/', views.resultado_influencer),
    path('crear_plataforma/', views.plataforma_formulario, name='Plataformas'),
    path('buscar_plataforma/', views.buscar_plataforma, name='BuscarPlataforma'),
    path('resultado_plataforma/', views.resultado_plataforma),
]