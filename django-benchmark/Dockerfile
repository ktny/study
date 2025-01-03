FROM python:3.11-slim

RUN apt upgrade -y && apt update -y
RUN apt install -y gcc
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./src/pyproject.toml ./src/poetry.lock ./
RUN poetry install
