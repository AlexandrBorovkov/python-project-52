install:
	uv sync

build:
	./build.sh

lint:
	uv run ruff check

start:
	uv run python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

check:
	uv run manage.py check

test:
	uv run manage.py test