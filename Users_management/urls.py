from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, AuthenticateUserView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('authenticate/', AuthenticateUserView.as_view(), name='authenticate'),
]
urlpatterns += router.urls
