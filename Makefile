MANAGE := poetry run python3 manage.py

install:
		poetry install

migrate:
		${MANAGE} makemigrations
		${MANAGE} migrate

lint:
		poetry run flake8 --exclude=migrations,admin.py,settings.py\
		task_manager

test:
		poetry run python3 manage.py test

test-coverage:
		poetry run coverage run --source='.' manage.py test
		poetry run coverage xml

PORT ?= 8000
dev:
		${MANAGE} runserver

start:
		poetry run gunicorn -w 5 -b 0.0.0.0:${PORT} task_manager.wsgi