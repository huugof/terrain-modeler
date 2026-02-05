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
    && rm -rf /var/lib/apt/lists/*

# Create an isolated venv to avoid system Python package conflicts
RUN python3.11 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip

WORKDIR /app

COPY pyproject.toml README.md /app/
COPY src /app/src

RUN pip install -e . && \
    pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers", "1", "--threads", "8", "va_lidar_context.webapp:app"]
