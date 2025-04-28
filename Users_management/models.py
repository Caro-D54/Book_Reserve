from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, correo, contrasena=None, **extra_fields):
        if not correo:
            raise ValueError('El correo es obligatorio')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo, contrasena, **extra_fields)
    
class User(AbstractBaseUser):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'correo']

    objects = UserManager()

    def __str__(self):
        return self.correo
    