BACKEND_DIR := backend
UV_CACHE_DIR ?= /tmp/uv-cache
MANAGE := UV_CACHE_DIR=$(UV_CACHE_DIR) uv run python manage.py
APP ?= platform

.PHONY: check makemigrations migrate test test-app runserver

check:
	cd $(BACKEND_DIR) && $(MANAGE) check

makemigrations:
	cd $(BACKEND_DIR) && $(MANAGE) makemigrations

migrate:
	cd $(BACKEND_DIR) && $(MANAGE) migrate

test:
	cd $(BACKEND_DIR) && $(MANAGE) test

test-app:
	cd $(BACKEND_DIR) && $(MANAGE) test apps.$(APP)

runserver:
	cd $(BACKEND_DIR) && $(MANAGE) runserver
