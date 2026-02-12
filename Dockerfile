FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    curl \
    ca-certificates \
    gnupg \
    dirmngr \
    && add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y --no-install-recommends \
    pdal \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    proj-bin \
    python3.11 \
    python3.11-venv \
    python3.11-distutils \
    libcap2-bin \
    && rm -rf /var/lib/apt/lists/*

# Create an isolated venv to avoid system Python package conflicts
RUN python3.11 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip

WORKDIR /app

COPY pyproject.toml README.md /app/
COPY src /app/src
COPY gunicorn.conf.py /app/gunicorn.conf.py

RUN pip install -e . && \
    pip install gunicorn

RUN useradd -m -u 10001 appuser && \
    mkdir -p /data/out /data/app && \
    chown -R appuser:appuser /app /data

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/healthz || exit 1

USER appuser

CMD ["gunicorn", "-c", "/app/gunicorn.conf.py", "va_lidar_context.webapp:app"]
