FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    pdal \
    libcap2-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md /app/
COPY src /app/src
COPY gunicorn.conf.py /app/gunicorn.conf.py

RUN pip install --upgrade pip && \
    pip install -e . && \
    pip install gunicorn

RUN useradd -m -u 10001 appuser && \
    mkdir -p /data/out /data/app && \
    chown -R appuser:appuser /app /data

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/healthz || exit 1

USER appuser

CMD ["gunicorn", "-c", "/app/gunicorn.conf.py", "va_lidar_context.webapp:app"]
