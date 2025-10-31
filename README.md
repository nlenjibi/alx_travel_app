# alx_travel_app

This repository contains a Django project scaffold configured for Django REST Framework, CORS, MySQL via environment variables (django-environ), Celery (RabbitMQ broker), and Swagger API documentation via drf-yasg.

Quick start

1. Create and activate a virtual environment and install dependencies:

   pip install -r alx_travel_app/requirement.txt

2. Copy the example env and update values:

   copy .env.example .env

   # then edit .env and set SECRET_KEY, DATABASE_URL, etc.

3. Apply migrations and run the server:

   python manage.py migrate
   python manage.py runserver

4. Open the Swagger UI:

   http://127.0.0.1:8000/swagger/

Notes

- Database: `DATABASE_URL` should be in the form `mysql://USER:PASSWORD@HOST:PORT/NAME`.
- Celery: configure `CELERY_BROKER_URL` in your `.env` (e.g. RabbitMQ `amqp://...`).
- This scaffold uses `django-environ` to read `.env` from the project root.
