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
    try:
        ctd = int(request.GET["tbCantidad"]) # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1

    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 0.068, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.050, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 0.065, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 4.07, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 37.94, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 177.15, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.041, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round( ctd * 3.79, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoMexicano.html', _dContenedor)

def convertir_PesoColombiano(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 0.00038, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.00028, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 0.00036, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 0.023, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 0.21, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 0.0056, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.00023, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 0.021, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoColombiano.html', _dContenedor)

def convertir_PesoChileno(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 0.0018, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.0013, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 0.0017, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 0.11, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 4.67, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 0.026, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.0011, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 0.1, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoChileno.html', _dContenedor)

def convertir_PesoArgentino(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 0.0017, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.012, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 0.016, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 9.33, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 43.57, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 0.25, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.01, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 0.93, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/PesoArgentino.html', _dContenedor)

def convertir_DolarAmericano(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 1.36, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 1.29, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 81.44, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 760, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 3548.5, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 20.03, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.83, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 75.83, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/DolarAmericano.html', _dContenedor)

def convertir_DolarCanadiense(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 1.05, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.77, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 62.91, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 587.13, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 2741.36, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 15.48, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.64, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 58.61, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/DolarCanadiense.html', _dContenedor)

def convertir_DolarAustraliano(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.074, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 0.95, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 60, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 560.1, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 2614.57, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 14.76, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.61, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 55.9, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/DolarAustraliano.html', _dContenedor)

def convertir_Euro(request):
    try:
        ctd = request.GET["tbCantidad"] # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 1.64, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 1.21, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 1.56, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 98.26, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 917.05, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 4281.76, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 24.17, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd * 91.53, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/Euro.html', _dContenedor)

def convertir_Rublo(request):
    try:
        ctd = int(request.GET["tbCantidad"]) # obtener cantidad recibida por GET
    except KeyError:
        ctd = -1
    
    # El diccionario contenedor incluye una clave cuyo valor será el diccionario 
    # que será lleno de las conversiones, esto, para realizar el for each 
    _dContenedor, _dConversion = {}, {} # Diccionarios para el envio de valores

    # Manipulación de los datos
    _dConversion['Dolar Australiano'] = 0 if ctd == -1 else round(ctd * 0.018, 3)
    _dConversion['Dolar Americano'] = 0 if ctd == -1 else round(ctd * 0.013, 3)
    _dConversion['Dolar Canadiense'] = 0 if ctd == -1 else round(ctd * 0.017, 3)
    _dConversion['Peso argetino'] = 0 if ctd == -1 else round(ctd * 1.07, 3)
    _dConversion['Peso chileno'] = 0 if ctd == -1 else round(ctd * 10.02, 3)
    _dConversion['Peso colombiano'] = 0 if ctd == -1 else round(ctd * 46.77, 3)
    _dConversion['Peso mexicano'] = 0 if ctd == -1 else round(ctd * 0.26, 3)
    _dConversion['Euro'] = 0 if ctd == -1 else round(ctd * 0.011, 3)
    _dConversion['Rublo ruso'] = 0 if ctd == -1 else round(ctd, 3)

    _dContenedor['conversiones'] = _dConversion
    return render(request, 'ProyectoWebApp/Rublo.html', _dContenedor)
