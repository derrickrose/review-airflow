# install airflow wsl (preference ubuntu 18)

https://towardsdatascience.com/run-apache-airflow-on-windows-10-without-docker-3c5754bb98b4

* Note to set airflow home inside the wsl to avoid access error
mkdir airflow_home 
  pwd to get the path
example export AIRFLOW_HOME=/home/frils/airflow_home



create user 
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin



warning
 WARNING: The script pyjwt is installed in '/home/frils/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pybabel is installed in '/home/frils/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script email_validator is installed in '/home/frils/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script openapi-spec-validator is installed in '/home/frils/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script fabmanager is installed in '/home/frils/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script airflow is installed in '/home/frils/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.