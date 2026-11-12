# Tahap 1: build aplikasi
FROM python:3.14-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY . .

RUN SECRET_KEY=build-only-secret \
    DEBUG=False \
    ALLOWED_HOSTS=localhost \
    uv run --no-sync python manage.py collectstatic --noinput

# Tahap 2: image untuk menjalankan aplikasi
FROM python:3.14-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

COPY --from=builder /app /app

RUN mkdir -p /app/media /app/staticfiles \
    && groupadd --system django \
    && useradd --system --gid django django \
    && chown -R django:django /app

USER django

EXPOSE 8000

CMD ["sh", "-c", "uv run --no-sync python manage.py migrate && exec uv run --no-sync gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
