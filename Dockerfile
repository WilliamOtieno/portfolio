FROM python:3.7.3-alpine

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:$PORT