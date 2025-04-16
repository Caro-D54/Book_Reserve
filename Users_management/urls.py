from django.urls import path
from .views import RegisterView, AutheticateUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),name='register',
    path('authenticate/', AutheticateUserView.as_view()),name='authenticate',                  
]   
