from django.urls import path
from .views import EmailTokenObtainPairView, MeView, register_user
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('register/', register_user, name='register'),
]