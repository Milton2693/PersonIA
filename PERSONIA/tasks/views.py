from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from flask import Flask,render_template
from tasks.explorer import explorer
import nltk
from nltk.corpus import stopwords

# Create your views here.

nltk.download('stopwords')
stopwords_es = stopwords.words('spanish')
explorer_service = explorer(stopwords_es)

from django.shortcuts import render

def mi_vista(request):
    if request.method == 'POST':
        valor = request.POST['mi_campo']
        trigramas_image = explorer_service.generate_trigramas(int(valor))
    
        context = {
            'trigramas_image': trigramas_image
        }
    
        return render(request, 'trigramas.html', context)
    else:
        return render(request, 'trigramas.html')

def vista_login(request):
    if request.method == 'POST':
        usuario_valido = request.POST['mi_usuario']
        contraseña_valida = request.POST['mi_contraseña']
        usuarios_personia = [
            ['persona', 'personIA'],
            ['medellin','personIA'],
            ['personeria','personIA']
        ]

        if usuario_valido == usuarios_personia[0][0] and contraseña_valida == usuarios_personia[0][1]:
                return render(request, 'preHome.html')
        else:
            return render(request, 'loginIn.html')
    else:
        return render(request, 'loginIn.html')   
    
def login(request):
    return render(request,'loginIn.html',{
        'formLoginIn': AuthenticationForm
    })

def home(request):
    return render(request,'home.html')

def preHome(request):
    return render(request,'preHome.html')

def wordcloud(request):

    wordcloud_image = explorer_service.generate_word_cloud()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'wordcloud_image': wordcloud_image
    }
    
    return render(request, 'wordcloud.html', context)

def trigramas(request):
   return request

def eventos(request):

    dia, sura, eps, savia = explorer_service.generate_eventos()
    dia_image = dia 
    sura_image = sura
    eps_image = eps
    savia_image = savia

    context = {
        'dia_image': dia_image,
        'sura_image': sura_image,
        'eps_image': eps_image,
        'savia_image': savia_image
    }
    
    return render(request, 'eventos.html', context)

def topicos(request):

    topicos_image = explorer_service.generate_topicos()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'topicos_image': topicos_image
    }
    
    return render(request, 'topicos.html', context)

def temas(request):

    temas_image = explorer_service.generate_temas()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'temas_image': temas_image
    }
    
    return render(request, 'temas.html', context)

def subtemas(request):

    subtemas_image = explorer_service.generate_subtemas()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'subtemas_image': subtemas_image
    }
    
    return render(request, 'subtemas.html', context)

def comunas(request):

    comunas_image = explorer_service.generate_comunas()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'comunas_image': comunas_image
    }
    
    return render(request, 'comunas.html', context)

def municipios(request):

    municipios_image = explorer_service.generate_municipios()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'municipios_image': municipios_image
    }
    
    return render(request, 'municipios.html', context)

def servicios(request):

    servicios_image = explorer_service.generate_servicios()  # Supongamos que tienes una función que genera la imagen de la nube de palabras
    
    context = {
        'servicios_image': servicios_image
    }
    
    return render(request, 'servicios.html', context)