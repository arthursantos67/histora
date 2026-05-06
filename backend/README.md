# Backend

Django backend for Histora.

The backend runs inside Docker Compose. The host machine should only need Docker;
Python and `uv` are installed and executed inside the backend container.

## Runtime

- Python 3.14
- Django + Django REST Framework
- PostgreSQL
- Redis
- Dependency management with `uv` inside Docker

The backend is organized by domain under `backend/apps/`.

- `apps/platform`: platform-level concerns such as health and operational endpoints
- `apps/accounts`: custom user model and authentication endpoints

## Commands

Run common workflows from the repository root:

```bash
make build
make up
make down
make check
make makemigrations
make migrate
make test
make test-app APP=accounts
make shell
```

The `make` commands call `docker compose` and run Django inside the `web`
container. For direct one-off commands, use:

```bash
docker compose run --rm web python manage.py check
docker compose run --rm web python manage.py migrate
docker compose run --rm web python manage.py test apps.accounts
```

If the backend container is already running, commands can also be executed with:

```bash
docker compose exec web python manage.py check
```

Start the local development environment:

```bash
make up
```

The backend is available at `http://localhost:8000` with live reload enabled by
the bind mount in `docker-compose.yml`.

The project defaults to `config.settings.dev`. To load production settings
explicitly, set:

```bash
DJANGO_SETTINGS_MODULE=config.settings.prod
```
