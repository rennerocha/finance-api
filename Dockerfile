FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY settings.toml /app/settings.toml
COPY ./finance_api /app/app