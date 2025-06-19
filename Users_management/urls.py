from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, AuthenticateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('authenticate/', AuthenticateUserView.as_view(), name='authenticate'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += router.urls
