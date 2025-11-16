from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        mail = attrs.get('mail')
        password = attrs.get('password')

        if not mail or not password:
            raise serializers.ValidationError('Mail o contraseña inválidos')
        
        user = authenticate(mail=mail, password=password)
        if user is None:
            user = authenticate(mail=mail, password=password)
            if user is None:
                raise AuthenticationFailed('Mail o contraseña inválidos')
            
            data = super().validate({'mail': mail, 'password': password})
            data['user_id'] = user.id
            data['mail'] = user.mail
            data['name'] = getattr(user, 'name', None)
            return data