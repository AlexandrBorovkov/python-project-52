install:
	uv sync

build:
	./build.sh

start:
	uv run python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

selfcheck:
	uv run manage.py check

lint:
	uv run ruff check

test:
	uv run manage.py test

check: selfcheck lint test