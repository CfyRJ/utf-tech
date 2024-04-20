install:
	poetry install

start-debug:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test

lint:
	poetry run flake8 utf_tech
