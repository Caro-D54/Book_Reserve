from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import UserSerializer

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(mail="test@example.com", password="secret123", name="Test User")
        self.assertEqual(user.mail, "test@example.com")
        self.assertTrue(user.check_password("secret123"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(mail="admin@example.com", password="admin123", name="Admin")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)


class UserSerializerTest(TestCase):
    def test_serializer_hides_password(self):
        user = User.objects.create_user(mail="s@example.com", password="secret123", name="Serializer User")
        serializer = UserSerializer(user)
        data = serializer.data
        # El campo password no debe aparecer en la salida
        self.assertNotIn("password", data)
        self.assertEqual(data["mail"], "s@example.com")

    def test_serializer_creates_user_with_password(self):
        payload = {"mail": "new@example.com", "name": "New User", "password": "newpass123"}
        serializer = UserSerializer(data=payload)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertTrue(user.check_password("newpass123"))


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = "/api/auth/register/"   # ajusta según tus rutas reales
        self.login_url = "/api/auth/login/"

    def test_register_endpoint(self):
        payload = {"mail": "api@example.com", "name": "API User", "password": "apipass123"}
        response = self.client.post(self.register_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(mail="api@example.com").exists())

    def test_login_endpoint(self):
        User.objects.create_user(mail="login@example.com", password="login123", name="Login User")
        response = self.client.post(self.login_url, {"mail": "login@example.com", "password": "login123"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)  # ajusta según tu backend (puede ser 'access' o 'jwt')