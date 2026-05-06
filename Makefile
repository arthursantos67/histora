COMPOSE := docker compose
MANAGE := $(COMPOSE) run --rm web python manage.py
APP ?= platform

.PHONY: build up down logs shell check makemigrations migrate test test-app runserver

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up --build web

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f web

shell:
	$(MANAGE) shell

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

check:
	$(MANAGE) check

test:
	$(MANAGE) test

test-app:
	$(MANAGE) test apps.$(APP)

runserver:
	$(MAKE) up
