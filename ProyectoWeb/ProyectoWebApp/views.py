from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ProyectoWebApp/index.html')

# Vistas para mostrar el documento HTML, sin procesamiento de datos
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

# Vistas para mostrar el documento HTML, con procesamiento de datos
# Fecha en la que se revisaron las equivalencias de las monedas: 1 de diciembre de 2020
# Datos proporcionados por Google
def convertir_PesoMexicano(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 

    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 0.068
    _dConversion['Dolar Americano'] = ctd * 0.050
    _dConversion['Dolar Canadiense'] = ctd * 0.065
    _dConversion['Peso argetino'] = ctd * 4.07
    _dConversion['Peso chileno'] = ctd * 37.94
    _dConversion['Peso colombiano'] = ctd * 177.15
    _dConversion['Peso mexicano'] = ctd
    _dConversion['Euro'] = ctd * 0.041
    _dConversion['Rublo ruso'] = ctd * 3.79

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoMexicano.html', _dContenedor)

def convertir_PesoColombiano(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 0.00038
    _dConversion['Dolar Americano'] = ctd * 0.00028
    _dConversion['Dolar Canadiense'] = ctd * 0.00036
    _dConversion['Peso argetino'] = ctd * 0.023
    _dConversion['Peso chileno'] = ctd * 0.21
    _dConversion['Peso colombiano'] = ctd
    _dConversion['Peso mexicano'] = ctd * 0.0056
    _dConversion['Euro'] = ctd * 0.00023
    _dConversion['Rublo ruso'] = ctd * 0.021

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoColombiano.html')

def convertir_PesoChileno(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 0.0018
    _dConversion['Dolar Americano'] = ctd * 0.0013
    _dConversion['Dolar Canadiense'] = ctd * 0.0017
    _dConversion['Peso argetino'] = ctd * 0.11
    _dConversion['Peso chileno'] = ctd
    _dConversion['Peso colombiano'] = ctd * 4.67
    _dConversion['Peso mexicano'] = ctd * 0.026
    _dConversion['Euro'] = ctd * 0.0011
    _dConversion['Rublo ruso'] = ctd * 0.1

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoChileno.html')

def convertir_PesoArgentino(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 0.0017
    _dConversion['Dolar Americano'] = ctd * 0.012
    _dConversion['Dolar Canadiense'] = ctd * 0.016
    _dConversion['Peso argetino'] = ctd
    _dConversion['Peso chileno'] = ctd * 9.33
    _dConversion['Peso colombiano'] = ctd * 43.57
    _dConversion['Peso mexicano'] = ctd * 0.25
    _dConversion['Euro'] = ctd * 0.01
    _dConversion['Rublo ruso'] = ctd * 0.93

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoArgentino.html')

def convertir_DolarAmericano(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 1.36
    _dConversion['Dolar Americano'] = ctd
    _dConversion['Dolar Canadiense'] = ctd * 1.29
    _dConversion['Peso argetino'] = ctd * 81.44
    _dConversion['Peso chileno'] = ctd * 760
    _dConversion['Peso colombiano'] = ctd * 3548.5
    _dConversion['Peso mexicano'] = ctd * 20.03
    _dConversion['Euro'] = ctd * 0.83
    _dConversion['Rublo ruso'] = ctd * 75.83

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/DolarAmericano.html')

def convertir_DolarCanadiense(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 1.05
    _dConversion['Dolar Americano'] = ctd * 0.77
    _dConversion['Dolar Canadiense'] = ctd
    _dConversion['Peso argetino'] = ctd * 62.91
    _dConversion['Peso chileno'] = ctd * 587.13
    _dConversion['Peso colombiano'] = ctd * 2741.36
    _dConversion['Peso mexicano'] = ctd * 15.48
    _dConversion['Euro'] = ctd * 0.64
    _dConversion['Rublo ruso'] = ctd * 58.61

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/DolarCanadiense.html')

def convertir_DolarAustraliano(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd
    _dConversion['Dolar Americano'] = ctd * 0.074
    _dConversion['Dolar Canadiense'] = ctd * 0.95
    _dConversion['Peso argetino'] = ctd * 60
    _dConversion['Peso chileno'] = ctd * 560.1
    _dConversion['Peso colombiano'] = ctd * 2614.57
    _dConversion['Peso mexicano'] = ctd * 14.76
    _dConversion['Euro'] = ctd * 0.61
    _dConversion['Rublo ruso'] = ctd * 55.9

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/DolarAustraliano.html')

def convertir_Euro(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 1.64
    _dConversion['Dolar Americano'] = ctd * 1.21
    _dConversion['Dolar Canadiense'] = ctd * 1.56
    _dConversion['Peso argetino'] = ctd * 98.26
    _dConversion['Peso chileno'] = ctd * 917.05
    _dConversion['Peso colombiano'] = ctd * 4281.76
    _dConversion['Peso mexicano'] = ctd * 24.17
    _dConversion['Euro'] = ctd
    _dConversion['Rublo ruso'] = ctd * 91.53

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/Euro.html')

def convertir_Rublo(request):
    ctd = int(request.POST.get("tbCantidad")) # obtener cantidad recibida por POST 
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = ctd * 0.018
    _dConversion['Dolar Americano'] = ctd * 0.013
    _dConversion['Dolar Canadiense'] = ctd * 0.017
    _dConversion['Peso argetino'] = ctd * 1.07
    _dConversion['Peso chileno'] = ctd * 10.02
    _dConversion['Peso colombiano'] = ctd * 46.77
    _dConversion['Peso mexicano'] = ctd * 0.26
    _dConversion['Euro'] = ctd * 0.011
    _dConversion['Rublo ruso'] = ctd

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/Rublo.html')
