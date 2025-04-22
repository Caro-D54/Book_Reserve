from django.urls import path
from .views import CreateUserView, AuthenticateUserView

urlpatterns = [
    path('create_user/', CreateUserView.as_view()),
    path('authenticate_user/', AuthenticateUserView.as_view()),
]
