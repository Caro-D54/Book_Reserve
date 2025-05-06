from django.contrib.auth.backends import ModelBackend
from Users_management.models import User

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, correo=None, contrasena=None, **kwargs):
        try:
            user = User.objects.get(correo=correo)
        except User.DoesNotExist:
            return None
        if user.check_password(contrasena):
            return user
        return None