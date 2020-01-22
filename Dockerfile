# Pull base image
FROM python:3.8.1-slim

# Install system dependencies
RUN apt-get update
RUN apt-get install git -y

# Set environment varibles
ENV DJANGO_ENV=dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.0.0

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Create dynamic directories
RUN mkdir /code /logs /uploads /code/apps /code/conf

# Set work directory
WORKDIR /code

# Install project dependencies
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == prod && echo "--no-dev") --no-interaction --no-ansi --no-root
