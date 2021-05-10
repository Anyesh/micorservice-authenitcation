FROM python:latest

WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8301

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
RUN python manage.py makemigrations && python manage.py migrate --run-syncdb
CMD gunicorn --bind :8302 authentication.wsgi:application
