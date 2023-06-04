from django.urls import path, include
from . views import *


urlpatterns = [
    path('registro/',RegistroUsuarioView.as_view(), name='registro'),
    path('api-token-auth/', InicioSesionView.as_view())
]
