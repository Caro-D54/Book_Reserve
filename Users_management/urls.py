from django.urls import path
from .views import MailTokenObtainPairView, MeView, register_user, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('register/', register_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]