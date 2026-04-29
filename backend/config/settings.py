import os
from pathlib import Path
from urllib.parse import unquote, urlparse


def get_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


def get_list(name: str, default: list[str] | None = None) -> list[str]:
    value = os.getenv(name)
    if value is None:
        return list(default or [])
    return [item.strip() for item in value.split(",") if item.strip()]


def get_default_database() -> dict[str, str | Path]:
    return {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / os.getenv("SQLITE_PATH", "db.sqlite3"),
    }


def get_postgres_database() -> dict[str, str | int]:
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", ""),
        "USER": os.getenv("POSTGRES_USER", ""),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": int(os.getenv("POSTGRES_PORT", "5432")),
    }


def get_database_config() -> dict[str, str | int | Path]:
    database_url = os.getenv("DATABASE_URL")
    if not database_url and os.getenv("POSTGRES_DB"):
        return get_postgres_database()

    if not database_url:
        return get_default_database()

    parsed = urlparse(database_url)
    scheme = parsed.scheme.lower()

    if scheme in {"sqlite", "sqlite3"}:
        if parsed.path in {"", "/"}:
            return get_default_database()
        sqlite_path = unquote(parsed.path)
        if sqlite_path.startswith("/"):
            sqlite_path = sqlite_path[1:]
        return {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / sqlite_path,
        }

    if scheme in {"postgres", "postgresql", "pgsql"}:
        return {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": unquote(parsed.path.lstrip("/")),
            "USER": unquote(parsed.username or ""),
            "PASSWORD": unquote(parsed.password or ""),
            "HOST": parsed.hostname or os.getenv("POSTGRES_HOST", "localhost"),
            "PORT": parsed.port or int(os.getenv("POSTGRES_PORT", "5432")),
        }

    raise ValueError(
        "Unsupported DATABASE_URL scheme. Use sqlite:/// or postgresql://"
    )


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-me-before-production",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = get_list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "apps.platform.apps.PlatformConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': get_database_config(),
}

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = os.getenv("DJANGO_LANGUAGE_CODE", "en-us")

TIME_ZONE = os.getenv("DJANGO_TIME_ZONE", "UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = os.getenv("DJANGO_STATIC_URL", "static/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
