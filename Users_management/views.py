from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

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
