from django.shortcuts import render
from AppGenerica.models import *
from AppGenerica.forms import *
from django.http import HttpResponse


# Creo mis views

def inicio(request):

    return render(request, r'inicio.html')

# Creo mis formularios

def juego_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_juego_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            juego = Juego(nombre=informacion['nombre'],
                          empresa=informacion['empresa'],
                          categoria=informacion['categoria'],
                          jugadores=informacion['jugadores'])
            juego.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_juego_formulario()
    
    return render(request, r'juego.html', {'mi_formulario':mi_formulario})



def influencer_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_influencer_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            influencer = Influencer(nombre=informacion['nombre'],
                                    nacimiento=informacion['nacimiento'])
            
            influencer.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_influencer_formulario()
    
    return render(request, r'influencer.html', {'mi_formulario':mi_formulario})


def plataforma_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_plataforma_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            plataforma = Plataforma(nombre=informacion['nombre'],
                                    ceo=informacion['ceo'])
            
            plataforma.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_plataforma_formulario()
    
    return render(request, r'plataforma.html', {'mi_formulario':mi_formulario})








# Creo las busquedas en la DB

def buscar_juego(request):

    return render(request, r'buscar_juego.html')

def resultado_juego(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        empresa = Juego.objects.filter(nombre__icontains=nombre)
        categoria = Juego.objects.filter(nombre__icontains=nombre)
        jugadores = Juego.objects.filter(nombre__icontains=nombre)

        return render(request, r'resultado_juego.html', {"nombre":nombre,
                                                      "empresa":empresa,
                                                      "categoria":categoria,
                                                      "jugadores":jugadores})
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)







def buscar_influencer(request):

    return render(request, r'buscar_influencer.html')

def resultado_influencer(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        nacimiento = Influencer.objects.filter(nombre__icontains=nombre)

        return render(request, r'resultado_influencer.html', {"nombre":nombre,
                                                           "nacimiento":nacimiento})
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)








def buscar_plataforma(request):

    return render(request, r'buscar_plataforma.html')

def resultado_plataforma(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        ceo = Plataforma.objects.filter(nombre__icontains=nombre)

        return render(request, r'resultado_plataforma.html', {"nombre":nombre,
                                                           "ceo":ceo})
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)