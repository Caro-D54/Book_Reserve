from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, mail, password=None, **extra_fields):
        if not mail:
            raise ValueError('El correo es obligatorio')
        mail = self.normalize_email(mail)
        user = self.model(mail=mail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superuser debe tener is_superuser=True.')

        return self.create_user(mail, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    mail = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.mail