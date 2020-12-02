from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.index, name='Index'),
    # name es el nombre por el cual invocas al hacer los href en los html
    # El primer argumento del path y el name puedes ser nombres diferentes, no pasa nada

    # Vistas para el renderizado de los documentos sin procesamiento de información
    path('PesoChileno', views.PesoChileno, name='PesoChileno'),
    path('PesoMexicano', views.PesoMexicano, name='PesoMexicano'),
    path('PesoArgentino', views.PesoArgentino, name='PesoArgentino'),
    path('PesoColombiano', views.PesoColombiano, name='PesoColombiano'),

    path('DolarAmericano', views.DolarAmericano, name='DolarAmericano'),
    path('DolarCanadiense', views.DolarCanadiense, name='DolarCanadiense'),
    path('DolarAustraliano', views.DolarAustraliano, name='DolarAustraliano'),

    path('Euro', views.Euro, name='Euro'),
    path('Rublo', views.Rublo, name='Rublo'),

    # Vistas para el renderizado de los documentos con procesamiento de información
    path('convertir_PesoChileno', views.convertir_PesoChileno, name='convertir_PesoChileno'),
    path('convertir_PesoMexicano/', views.convertir_PesoMexicano, name='convertir_PesoMexicano'),
    path('convertir_PesoArgentino', views.convertir_PesoArgentino, name='convertir_PesoArgentino'),
    path('convertir_PesoColombiano', views.convertir_PesoColombiano, name='convertir_PesoColombiano'),

    path('convertir_DolarAmericano', views.convertir_DolarAmericano, name='convertir_DolarAmericano'),
    path('convertir_DolarCanadiense', views.convertir_DolarCanadiense, name='convertir_DolarCanadiense'),
    path('convertir_DolarAustraliano', views.convertir_DolarAustraliano, name='convertir_DolarAustraliano'),

    path('convertir_Euro', views.convertir_Euro, name='convertir_Euro'),
    path('convertir_Rublo', views.convertir_Rublo, name='convertir_Rublo'),
]