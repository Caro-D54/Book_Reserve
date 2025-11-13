from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, mail=None, password=None, **kwargs):
        mail = mail or kwargs.get('mail')
        if not mail or not password:
            return None
        try:
            user = User.objects.get(mail=mail)
        except User.DoesNotExist:
            return None
        return user if user.check_password(password) else None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id).mail
        except User.DoesNotExist:
            return None