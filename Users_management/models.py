from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, mail, password=None, **extra_fields):
        if not mail:
            raise ValueError('El correo es obligatorio')
        email = self.normalize_email(mail)
        user = self.model(mail=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    
class User(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    mail = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    objects = UserManager()

    def __str__(self):
        return self.correo
    