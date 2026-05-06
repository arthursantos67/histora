from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.accounts.models import User, UserRole, UserStatus


class AuthenticationApiTests(APITestCase):
    def test_registration_creates_pending_member_with_hashed_password(self):
        response = self.client.post(
            "/api/v1/auth/register/",
            {
                "email": "marcela@example.com",
                "password": "HistoraPass123!",
                "first_name": "Marcela",
                "last_name": "Silva",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", response.json()["user"])

        user = User.objects.get(email="marcela@example.com")
        self.assertEqual(user.role, UserRole.MEMBER)
        self.assertEqual(user.status, UserStatus.PENDING)
        self.assertNotEqual(user.password, "HistoraPass123!")
        self.assertTrue(check_password("HistoraPass123!", user.password))

    def test_registration_validates_required_fields(self):
        response = self.client.post("/api/v1/auth/register/", {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            set(response.json().keys()),
            {"email", "password", "first_name", "last_name"},
        )

    def test_login_returns_token_for_active_user(self):
        user = User.objects.create_user(
            "active@example.com",
            password="HistoraPass123!",
            first_name="Ana",
            last_name="Costa",
            status=UserStatus.ACTIVE,
        )

        response = self.client.post(
            "/api/v1/auth/login/",
            {"email": "active@example.com", "password": "HistoraPass123!"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["token"], Token.objects.get(user=user).key)
        self.assertEqual(response.json()["user"]["email"], "active@example.com")

    def test_login_rejects_accounts_that_are_not_active(self):
        for account_status in (
            UserStatus.PENDING,
            UserStatus.SUSPENDED,
            UserStatus.BANNED,
        ):
            with self.subTest(account_status=account_status):
                User.objects.create_user(
                    f"{account_status}@example.com",
                    password="HistoraPass123!",
                    status=account_status,
                )

                response = self.client.post(
                    "/api/v1/auth/login/",
                    {
                        "email": f"{account_status}@example.com",
                        "password": "HistoraPass123!",
                    },
                    format="json",
                )

                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(
                    response.json()["non_field_errors"],
                    ["This account is not active."],
                )

    def test_current_user_endpoint_requires_authentication(self):
        response = self.client.get("/api/v1/auth/me/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_current_user_endpoint_returns_authenticated_user(self):
        user = User.objects.create_user(
            "me@example.com",
            password="HistoraPass123!",
            first_name="Lia",
            last_name="Pereira",
            status=UserStatus.ACTIVE,
        )
        token = Token.objects.create(user=user)

        response = self.client.get(
            "/api/v1/auth/me/",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()["user"],
            {
                "id": str(user.id),
                "email": "me@example.com",
                "first_name": "Lia",
                "last_name": "Pereira",
                "role": UserRole.MEMBER,
                "status": UserStatus.ACTIVE,
                "created_at": response.json()["user"]["created_at"],
                "updated_at": response.json()["user"]["updated_at"],
            },
        )

    def test_user_role_and_status_choices_match_prd(self):
        self.assertEqual(
            {choice.value for choice in UserRole},
            {"member", "moderator", "admin"},
        )
        self.assertEqual(
            {choice.value for choice in UserStatus},
            {"pending", "active", "suspended", "banned"},
        )
