from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.index, name='Index'),

    path('PesoChileno', views.convertir_PesoChileno, name='cPesoChileno'),
    path('PesoMexicano', views.convertir_PesoMexicano, name='cPesoMexicano'),
    path('PesoArgentino', views.convertir_PesoArgentino, name='cPesoArgentino'),
    path('PesoColombiano', views.convertir_PesoColombiano, name='cPesoColombiano'),

    path('DolarAmericano', views.convertir_DolarAmericano, name='cDolarAmericano'),
    path('DolarCanadiense', views.convertir_DolarCanadiense, name='cDolarCanadiense'),
    path('DolarAustraliano', views.convertir_DolarAustraliano, name='cDolarAustraliano'),

    path('Euro', views.convertir_Euro, name='cEuro'),
    path('Rublo', views.convertir_Rublo, name='cRublo'),
]