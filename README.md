# Histora

Histora is an academic social network for historians of education.
The project aims to combine a scientific repository and qualified social interaction in a single environment.

## Project Status

- Requirements document defined
- Dockerized Django backend initialized
- Initial authentication flow implemented

## MVP Goal

Deliver a web platform with:

- User registration and authentication
- Academic profiles
- Publications with PDF upload and versioning
- Chronological feed with endorsements and comments
- Basic moderation and reports

## Initial Scope (Planned Technologies)

- Backend: Django + Django REST Framework
- Frontend: Next.js
- Database: PostgreSQL
- Cache and rate limiting: Redis
- Local infrastructure: Docker Compose

## Current Structure

- product-requirements-document.md: functional and technical project specification
- backend/: Django API
- docker-compose.yml: local PostgreSQL, Redis, and backend services
- Makefile: Docker-first development commands

## Local Development

The project runs through Docker Compose. The host machine should not need a
local Python or `uv` installation for backend commands.

```bash
make build
make up
make check
make test
make test-app APP=accounts
make migrate
```

The backend is served at `http://localhost:8000`.

For direct Django commands, run them inside the `web` container:

```bash
docker compose run --rm web python manage.py check
docker compose run --rm web python manage.py test apps.accounts
```

## How to Contribute

1. Review the requirements document
2. Open issues with suggestions or scope adjustments
3. Propose small, objective improvements for the initial setup

## License

This project is under the license defined in LICENSE.
