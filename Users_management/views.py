from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models  import User
from .serializers import UserSerializer
from rest_framework import status

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthenticateUserView(APIView):
    def post(self, request):
        email = request.data.get('correo')
        password = request.data.get('contrasena')
        user = authenticate(username=email, password=password)
        if user is None:
            return Response({"mensaje": 'Usuario o contraseña incorrectos'}, status= status.HTTP_200_OK)
        else:
            return Response({"mensaje": 'Usuario autenticado'}, status= status.HTTP_401_UNAUTHORIZED)
    
