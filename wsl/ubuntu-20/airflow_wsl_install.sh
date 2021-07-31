## update the referencies to dependencies
sudo apt update && sudo apt upgrade -y

## install pip
sudo apt-get install software-properties-common -y
sudo apt-add-repository universe -y
sudo apt-get update -y
sudo apt-get install python3-pip -y

## install airflow
pip3 install apache-airflow

## create airflow home directory
mkdir -p /home/frils/airflow_home

## make environment variable airflow_home
export AIRFLOW_HOME=/home/frils/airflow_home

## test airflow installation
airflow info

#!/bin/bash


## automount and link drives to / 
WSL_CONF_FILE_NAME=wsl.conf
WSL_CONF_PATH="/etc/$WSL_CONF_FILE_NAME"
echo "[automount]" > $WSL_CONF_FILE_NAME
echo "root = /" >> $WSL_CONF_FILE_NAME
echo "options = \"metadata\"" >> $WSL_CONF_FILE_NAME

sudo mv $WSL_CONF_FILE_NAME $WSL_CONF_PATH
