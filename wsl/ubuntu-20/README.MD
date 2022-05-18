# install airflow wsl (preference ubuntu 20.04 LTS)

## prerequisites

* install wsl in windows 10
  https://docs.microsoft.com/fr-fr/windows/wsl/install
* install ubuntu 20.04 with user frils on top of wsl

## install apache airflow inside our new fresh wsl

* with a terminal opened, point to the directory of the installation script
  `cd PATH`
* run the installation script
  `./airflow_wsl_install.sh`

cf: https://towardsdatascience.com/run-apache-airflow-on-windows-10-without-docker-3c5754bb98b4

* Note to set airflow home inside the wsl to avoid access error mkdir airflow pwd to get the path example export
  AIRFLOW_HOME=/home/frils/airflow_home


* copy dags from dev directory to airflow dags directory

`cp -r /c/Users/fampi/Documents/izybe/review-airflow/dev/dags/ /home/frils/airflow`

* copy plugins from dev to airflow plugins (should restart both scheduler and webserver)

`cp -r /c/Users/fampi/Documents/izybe/review-airflow/dev/plugins/ /home/frils/airflow`
