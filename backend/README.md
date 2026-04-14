## Backend

Django backend initialized with `uv`.

### Commands

Install and sync dependencies:

```bash
uv sync
```

Run Python commands through `uv`:

```bash
uv run python manage.py check
uv run python manage.py migrate
uv run python manage.py runserver
```

Run the containerized development environment from the repository root:

```bash
docker compose up --build
```

The backend is available at `http://localhost:8000` with live reload enabled through the bind mount in `docker-compose.yml`.
