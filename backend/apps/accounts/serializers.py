from typing import Any, cast

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.accounts.models import User, UserRole, UserStatus


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
        }

    def validate_password(self, value: str):
        validate_password(value)
        return value

    def create(self, validated_data: dict[str, Any]):
        return User.objects.create_user(
            **validated_data,
            role=UserRole.MEMBER,
            status=UserStatus.PENDING,
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs: dict[str, Any]):
        request = self.context.get("request")
        user = cast(
            User | None,
            authenticate(
                request=request,
                username=attrs["email"],
                password=attrs["password"],
            ),
        )

        if user is None:
            raise serializers.ValidationError(
                {"non_field_errors": ["Unable to log in with provided credentials."]}
            )

        if not user.is_account_active:
            raise serializers.ValidationError(
                {"non_field_errors": ["This account is not active."]}
            )

        attrs["user"] = user
        return attrs
