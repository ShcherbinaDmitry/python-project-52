PORT ?= 8000
start:
		poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

dev:
		python3 manage.py runserver

activate:
		source .venv/bin/activate

compilemessages:
		python manage.py compilemessages

