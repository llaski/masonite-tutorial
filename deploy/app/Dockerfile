FROM python:3.7-stretch

ARG INCLUDE_DEV_PACKAGES=''

ENV GUNICORN_WORKERS=3
ENV GUNICORN_RELOAD=''

ENV PYTHONUNBUFFERED 1

RUN apt-get update

# RUN mkdir -p /usr/src/deploy
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8100

RUN pip install --upgrade pip
RUN pip install pipenv

# COPY ./pyproject.toml /usr/src/app/
# COPY ./poetry.lock /usr/src/app/

COPY . /usr/src/app

RUN pipenv install ${INCLUDE_DEV_PACKAGES} --system --deploy --ignore-pipfile

# RUN chmod +x /usr/src/app/deploy/app/entrypoint.sh

# COPY ./deploy/app/django.log /usr/src/app/storage/logs/django.log

# ENTRYPOINT ["sh", "/usr/src/app/deploy/app/entrypoint.sh"]

CMD gunicorn wsgi:application -b 0.0.0.0:8100 --workers ${GUNICORN_WORKERS} ${GUNICORN_RELOAD}
