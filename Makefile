install:
	poetry install

start-debug:
	poetry run python manage.py runserver

lint:
	poetry run flake8 utf_tech
