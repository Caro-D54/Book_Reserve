from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate, login

class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('correo')
        password = request.data.get('contrasena')
        
        if email and password:
            if not User.objects.filter(correo=email).exists():
                user = User.objects.create_user(email, password=password)
                return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class AuthenticateUserView(APIView):
    def post(self, request):
        email = request.data.get('correo')
        password = request.data.get('contrasena')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Usuario autenticado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no autenticado'}, status=status.HTTP_400_BAD_REQUEST)
    
