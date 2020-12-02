from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Index")

def convertir_PesoMexicano(request):
    return HttpResponse("Convertir pesos mexicanos")

def convertir_PesoColombiano(request):
    return HttpResponse("Convertir pesos colombianos")

def convertir_PesoChileno(request):
    return HttpResponse("Convertir pesos chilenos")

def convertir_PesoArgentino(request):
    return HttpResponse("Convertir pesos argentinos")

def convertir_DolarAmericano(request):
    return HttpResponse("Convertir dolar americano")

def convertir_DolarCanadiense(request):
    return HttpResponse("Convertir dolar canadiense")

def convertir_DolarAustraliano(request):
    return HttpResponse("Convertir dolar australiano")

def convertir_Euro(request):
    return HttpResponse("Convertir euros")

def convertir_Rublo(request):
    return HttpResponse("Convertir rublos")
