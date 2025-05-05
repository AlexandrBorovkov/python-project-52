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
	uv run manage.py test --keepdb --noinput --cov=task_manager --cov-report=xml

selfcheck:
	uv run manage.py check

check: selfcheck lint test-cov