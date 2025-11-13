from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthenticateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Router para el ViewSet de usuarios
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Endpoint de autenticación personalizada (si lo implementaste en views.py)
    path('api/authenticate/', AuthenticateUserView.as_view(), name='authenticate'),

    # Endpoints estándar de JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Endpoints generados automáticamente por el router (CRUD de usuarios)
    path('api/', include(router.urls)),
]