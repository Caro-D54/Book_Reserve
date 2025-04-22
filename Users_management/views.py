from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models  import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthenticateUserView(APIView):
    def post(self, request):
        email = request.data.get('correo')
        password = request.data.get('contrasena')
        
        return Response({"mensaje": 'Usuario autenticado correctamente'})
    
