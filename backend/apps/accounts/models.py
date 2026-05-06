from __future__ import annotations

import uuid
from typing import Any

from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models


class UserRole(models.TextChoices):
    MEMBER = "member", "Member"
    MODERATOR = "moderator", "Moderator"
    ADMIN = "admin", "Admin"


class UserStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    ACTIVE = "active", "Active"
    SUSPENDED = "suspended", "Suspended"
    BANNED = "banned", "Banned"


class UserManager(DjangoUserManager):
    use_in_migrations = True

    def create_user(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: Any,
    ):
        email = email or username
        if not email:
            raise ValueError("The email address is required.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: Any,
    ):
        extra_fields.setdefault("role", UserRole.ADMIN)
        extra_fields.setdefault("status", UserStatus.ACTIVE)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.MEMBER,
        db_index=True,
    )
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.PENDING,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        indexes = [
            models.Index(fields=["email"], name="idx_users_email"),
            models.Index(fields=["status"], name="idx_users_status"),
        ]

    def __str__(self):
        return self.email

    @property
    def is_account_active(self):
        return self.is_active and self.status == UserStatus.ACTIVE

    @property
    def can_moderate(self):
        return self.role in {UserRole.MODERATOR, UserRole.ADMIN}
