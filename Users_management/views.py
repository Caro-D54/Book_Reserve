from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

from Users_management.models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    CRUD de usuarios. Por defecto solo accesible para administradores.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # solo admin puede listar/crear usuarios


class AuthenticateUserView(APIView):
    """
    Vista de autenticación personalizada.
    Recibe mail y password, valida credenciales y devuelve tokens JWT.
    """
    def post(self, request):
        # Ajusta los nombres de los campos según lo que envíe tu frontend
        email = request.data.get('mail')       # tu modelo usa 'mail'
        password = request.data.get('password')

        user = authenticate(request, mail=email, password=password)

        if user is None:
            return Response(
                {"mensaje": "Usuario o contraseña incorrectos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Generar tokens JWT para el usuario autenticado
        refresh = RefreshToken.for_user(user)
        return Response({
            "mensaje": "Usuario autenticado",
            "user": {
                "id": user.id,
                "mail": user.mail,
                "name": user.name,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)