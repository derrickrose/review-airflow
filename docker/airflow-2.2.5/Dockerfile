FROM apache/airflow:2.2.5-python3.9

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
RUN pip install --user -r requirements.txt