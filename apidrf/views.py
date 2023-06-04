from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# vista para registrar un usuario
class RegistroUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #verificar si ya existe un usuario con los mismos valores
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        if User.objects.filter(username=username).exists():
            return Response({'error':'El nombre de usuario ya esta en uso'}, status=400)
        if User.objects.filter(username=email).exists():
            return Response({'error':'El email de usuario ya esta en uso'}, status=400)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,status=201,headers=headers)

# vista para que el usuario inicie sesion

"""
es posible crear una vista utilizando Django Rest Framework (DRF) para que los usuarios inicien sesión en tu API. DRF proporciona una vista llamada ObtainAuthToken que se puede utilizar para autenticar y generar tokens de acceso para los usuarios.
https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
"""
class InicioSesionView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,

        })
        
        