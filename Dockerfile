FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

RUN apt-get update && apt-get install -y --no-install-recommends \
    pdal \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    proj-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md /app/
COPY src /app/src

RUN python -m pip install --upgrade pip && \
    pip install -e . && \
    pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers", "1", "--threads", "8", "va_lidar_context.webapp:app"]
