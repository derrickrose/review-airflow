AIRFLOW_VERSION=2.1.2
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[async,postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow db init

airflow info



pip install apache-airflow-providers-amazon

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
	--password admin\
    --email spiderman@superhero.org