FROM apache/airflow:3.0.6-python3.12

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    software-properties-common \
    python3-dev \
    unixodbc-dev \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt .
RUN pip install -r requirements.txt
