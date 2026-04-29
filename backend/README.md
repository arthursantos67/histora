## Backend

Django backend initialized with `uv`.

### App layout

The backend is organized by domain under `backend/apps/`.

- `apps/platform`: platform-level concerns such as health and operational endpoints

This structure leaves room for future apps to be added with clearer domain boundaries.

### Commands

Install and sync dependencies:

```bash
uv sync
```

Run common workflows from the repository root:

```bash
make check
make makemigrations
make migrate
make test
make test-app APP=platform
make runserver
```

Run Python commands directly through `uv` from `backend/` when needed:

```bash
uv run python manage.py check
uv run python manage.py migrate
uv run python manage.py test apps.platform
uv run python manage.py runserver
```

Run the containerized development environment from the repository root:

```bash
docker compose up --build
```

The backend is available at `http://localhost:8000` with live reload enabled through the bind mount in `docker-compose.yml`.
