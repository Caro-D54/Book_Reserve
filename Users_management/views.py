from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer

User = get_user_model()

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        mail = request.data.get('mail')
        password = request.data.get('password')

        user = authenticate(request, mail=mail, password=password)
        if user is None:
            return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "mail": user.mail,
                "name": user.name,
                "is_staff": user.is_staff or user.is_superuser,
            }
        })
        

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "mail": user.mail,
                    "name": user.name,
                    "is_staff": user.is_staff or user.is_superuser,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
        

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Acceso Concedido para {request.user.mail}",
            "user_id": request.user.id,
            "mail": request.user.mail,
        })
    
class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        mail = attrs.get('mail') or attrs.get('username')
        password = attrs.get('password')

        if not mail or not password:
            raise serializers.ValidationError("Credenciales requeridas")

        user = authenticate(mail=mail, password=password)
        if user is None:
            user = authenticate(username=mail, password=password)
        if user is None:
            raise serializers.ValidationError("Credenciales incorrectas")

        data = super().validate({'username': user.mail, 'password': password})
        data['user_id'] = user.id
        data['mail'] = user.mail
        data['name'] = getattr(user, 'name', '')
        return data


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
