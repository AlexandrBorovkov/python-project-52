install:
	uv sync

build:
	./build.sh

start:
	uv run python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check

test:
	uv run manage.py test

test-cov:
	uv run manage.py test --keepdb --noinput --cov=myapp --cov-report=xml

check:
	lint test-cov