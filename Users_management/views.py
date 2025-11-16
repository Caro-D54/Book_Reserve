from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import EmailTokenObtainPairSerializer

User = get_user_model()

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    name = request.data.get('name')
    mail = request.data.get('mail')
    password = request.data.get('password')

    if not name or not mail or not password:
        return Response({'error': 'Todos los campos son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(mail=mail).exists():
        return Response({'error': 'El mail ya existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(name=name, mail=mail, password=password)
    refresh = RefreshToken.for_user(user)

    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user_id': user.id,
        'mail': user.mail,
        'name': user.name,
    }, status=status.HTTP_201_CREATED)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'mail': user.mail,
            'name': getattr(user, 'name', ''),
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active,
        })

'''
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
'''