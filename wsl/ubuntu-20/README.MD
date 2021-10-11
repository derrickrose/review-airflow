# install airflow wsl (preference ubuntu 18)

## prerequisites

install wsl ubuntu 20 with user frils

https://towardsdatascience.com/run-apache-airflow-on-windows-10-without-docker-3c5754bb98b4

* Note to set airflow home inside the wsl to avoid access error mkdir airflow pwd to get the path example export
  AIRFLOW_HOME=/home/frils/airflow_home


* copy dags from dev to airflow dags

> cp -r /d/review-airflow-wsl/dev/dags/ /home/frils/airflow

* copy plugins from dev to airflow plugins (should restart both scheduler and webserver)

> cp -r /d/review-airflow-wsl/dev/plugins/ /home/frils/airflow
