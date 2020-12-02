from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ProyectoWebApp/index.html')

def PesoMexicano(request):
    return render(request, 'ProyectoWebApp/PesoMexicano.html')

def PesoColombiano(request):
    return render(request, 'ProyectoWebApp/PesoColombiano.html')

def PesoChileno(request):
    return render(request, 'ProyectoWebApp/PesoChileno.html')

def PesoArgentino(request):
    return render(request, 'ProyectoWebApp/PesoArgentino.html')

def DolarAmericano(request):
    return render(request, 'ProyectoWebApp/DolarAmericano.html')

def DolarCanadiense(request):
    return render(request, 'ProyectoWebApp/DolarCanadiense.html')

def DolarAustraliano(request):
    return render(request, 'ProyectoWebApp/DolarAustraliano.html')

def Euro(request):
    return render(request, 'ProyectoWebApp/Euro.html')

def Rublo(request):
    return render(request, 'ProyectoWebApp/Rublo.html')

def convertir_PesoMexicano(request):
    return render(request, 'ProyectoWebApp/PesoMexicano.html')

def convertir_PesoColombiano(request):
    return render(request, 'ProyectoWebApp/PesoColombiano.html')

def convertir_PesoChileno(request):
    return render(request, 'ProyectoWebApp/PesoChileno.html')

def convertir_PesoArgentino(request):
    return render(request, 'ProyectoWebApp/PesoArgentino.html')

def convertir_DolarAmericano(request):
    return render(request, 'ProyectoWebApp/DolarAmericano.html')

def convertir_DolarCanadiense(request):
    return render(request, 'ProyectoWebApp/DolarCanadiense.html')

def convertir_DolarAustraliano(request):
    return render(request, 'ProyectoWebApp/DolarAustraliano.html')

def convertir_Euro(request):
    return render(request, 'ProyectoWebApp/Euro.html')

def convertir_Rublo(request):
    return render(request, 'ProyectoWebApp/Rublo.html')
