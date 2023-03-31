.PHONY: run
run:
	uvicorn bbs.asgi:application --host=127.0.0.1 --port=7000 --reload

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations
