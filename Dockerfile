FROM python:3.12-alpine

WORKDIR /application

RUN pip install uv

COPY pyproject.toml .
RUN uv venv; uv pip install -r pyproject.toml

COPY . .

EXPOSE 8000

CMD uv run alembic upgrade head; uv run python src/main.py