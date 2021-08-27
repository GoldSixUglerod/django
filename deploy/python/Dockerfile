FROM python:3.9

WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip poetry==1.1.6

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev
COPY . .

CMD poetry run python src/manage.py migrate && \
    poetry run src/manage.py runserver 0.0.0.0:8000
