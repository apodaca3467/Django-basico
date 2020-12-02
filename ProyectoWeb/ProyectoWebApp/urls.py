from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.index, name='Index'),
    # name es el nombre por el cual invocas al hacer los href en los html
    # El primer argumento del path y el name puedes ser nombres diferentes, no pasa nada
    path('PesoChileno', views.PesoChileno, name='PesoChileno'),
    path('PesoMexicano', views.PesoMexicano, name='PesoMexicano'),
    path('PesoArgentino', views.PesoArgentino, name='PesoArgentino'),
    path('PesoColombiano', views.PesoColombiano, name='PesoColombiano'),

    path('DolarAmericano', views.DolarAmericano, name='DolarAmericano'),
    path('DolarCanadiense', views.DolarCanadiense, name='DolarCanadiense'),
    path('DolarAustraliano', views.DolarAustraliano, name='DolarAustraliano'),

    path('Euro', views.Euro, name='Euro'),
    path('Rublo', views.Rublo, name='Rublo'),
]