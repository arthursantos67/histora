import os
from pathlib import Path
from urllib.parse import unquote, urlparse

DatabaseValue = str | int | Path
DatabaseConfig = dict[str, DatabaseValue]


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


def env_list(name: str, default: list[str] | None = None) -> list[str]:
    value = os.getenv(name)
    if value is None:
        return list(default or [])
    return [item.strip() for item in value.split(",") if item.strip()]


def default_database_config(base_dir: Path) -> DatabaseConfig:
    return {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": base_dir / os.getenv("SQLITE_PATH", "db.sqlite3"),
    }


def postgres_database_config() -> DatabaseConfig:
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", ""),
        "USER": os.getenv("POSTGRES_USER", ""),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": int(os.getenv("POSTGRES_PORT", "5432")),
    }


def database_config(base_dir: Path) -> DatabaseConfig:
    database_url = os.getenv("DATABASE_URL")
    if not database_url and os.getenv("POSTGRES_DB"):
        return postgres_database_config()

    if not database_url:
        return default_database_config(base_dir)

    parsed = urlparse(database_url)
    scheme = parsed.scheme.lower()

    if scheme in {"sqlite", "sqlite3"}:
        if parsed.path in {"", "/"}:
            return default_database_config(base_dir)
        sqlite_path = unquote(parsed.path)
        if sqlite_path.startswith("/"):
            sqlite_path = sqlite_path[1:]
        return {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": base_dir / sqlite_path,
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
