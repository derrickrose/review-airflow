## update the referencies to dependencies
sudo apt update && sudo apt upgrade -y

## install pip
sudo apt-get install software-properties-common -y
sudo apt-add-repository universe -y
sudo apt-get update -y
sudo apt-get install python3-pip -y

## install airflow
#pip3 install apache-airflow
AIRFLOW_VERSION=2.1.2
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
export PATH=$PATH:/home/frils/.local/bin/
pip3 install testresources
pip3 install "apache-airflow[async,postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

## create airflow home directory
mkdir -p /home/frils/airflow

## make environment variable airflow_home
export AIRFLOW_HOME=/home/frils/airflow

#install airflow dependencies for amazon
pip install apache-airflow-providers-amazon

## automount and link drives to /
WSL_CONF_FILE_NAME=wsl.conf
WSL_CONF_PATH="/etc/$WSL_CONF_FILE_NAME"
echo "[automount]" >$WSL_CONF_FILE_NAME
echo "root = /" >>$WSL_CONF_FILE_NAME
echo "options = \"metadata\"" >>$WSL_CONF_FILE_NAME
sudo mv $WSL_CONF_FILE_NAME $WSL_CONF_PATH

# show airflow conf
airflow info

# start airflow db
airflow db init

# create an airflow user
airflow users create \
  --username admin \
  --firstname Peter \
  --lastname Parker \
  --role Admin \
  --password admin \
  --email spiderman@superhero.org

# show airflow conf
airflow info
