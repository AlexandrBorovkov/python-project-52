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
	uv run coverage run manage.py test --keepdb --noinput
	uv run coverage xml -o coverage.xml --include="*"

selfcheck:
	uv run manage.py check

check: selfcheck lint test-cov