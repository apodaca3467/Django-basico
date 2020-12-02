from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.index, name='Index'),

    # name es el nombre por el cual invocas al hacer los href en los html
    path('PesoChileno', views.convertir_PesoChileno, name='pagina_PesoChileno'),
    path('PesoMexicano', views.convertir_PesoMexicano, name='pagina_PesoMexicano'),
    path('PesoArgentino', views.convertir_PesoArgentino, name='pagina_PesoArgentino'),
    path('PesoColombiano', views.convertir_PesoColombiano, name='pagina_PesoColombiano'),

    path('DolarAmericano', views.convertir_DolarAmericano, name='pagina_DolarAmericano'),
    path('DolarCanadiense', views.convertir_DolarCanadiense, name='pagina_DolarCanadiense'),
    path('DolarAustraliano', views.convertir_DolarAustraliano, name='pagina_DolarAustraliano'),

    path('Euro', views.convertir_Euro, name='pagina_Euro'),
    path('Rublo', views.convertir_Rublo, name='pagina_Rublo'),
]