from django.contrib import admin
from .models import User
# Register your models here.
 
admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion', 'fecha_devolucion')
    