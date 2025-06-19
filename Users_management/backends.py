from django.contrib.auth.backends import ModelBackend
from Users_management.models import User

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, mail=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=mail)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None