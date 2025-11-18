# Users_management/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

# --- Serializer para login con mail ---
class MailTokenObtainPairSerializer(serializers.Serializer):
    mail = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        mail = attrs.get("mail")
        password = attrs.get("password")

        if not mail or not password:
            raise serializers.ValidationError("Credenciales requeridas")

        # Autenticación usando mail como USERNAME_FIELD
        user = authenticate(mail=mail, password=password)
        if user is None:
            raise serializers.ValidationError("Credenciales incorrectas")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user_id": user.id,
            "mail": user.mail,
            "name": getattr(user, "name", None),
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        }

class MailTokenObtainPairView(TokenObtainPairView):
    serializer_class = MailTokenObtainPairSerializer


# --- Registro de usuario ---
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    mail = request.data.get("mail")
    name = request.data.get("name", "")
    password = request.data.get("password")

    if not mail or not password:
        return Response({"error": "Todos los campos son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(mail=mail).exists():
        return Response({"error": "El correo ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(mail=mail, password=password, name=name)
    refresh = RefreshToken.for_user(user)

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user_id": user.id,
        "mail": user.mail,
        "name": user.name,
    }, status=status.HTTP_201_CREATED)


# --- Vista de perfil del usuario autenticado ---
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "mail": user.mail,
            "name": getattr(user, "name", None),
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
            "is_active": user.is_active,
        })


# --- Logout (invalidar refresh token) ---
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "No se proporcionó refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Sesión cerrada"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Token inválido o ya caducado"}, status=status.HTTP_400_BAD_REQUEST)
