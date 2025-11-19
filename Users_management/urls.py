from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProtectedView, EmailTokenObtainPairView
from .views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedView.as_view(), name='users_protected'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]