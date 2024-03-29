# Mastering Airflow

--------------------------------------------------------------------------

## Running airflow on docker (using docker-compose)

### Setup airflow

```
docker-compose up airflow-init
```

### Run airflow

```
docker-compose up
```

## Running airflow on Ubuntu WSL

### Installing Ubuntu WSL

Airflow does not run on Windows, so it is recommended to install Ubuntu WSL (Windows Subsystem for Linux)

* Creating user profile, in my case username *frils* and password *frils* (be aware to synchronize the path to user's
  profile directory)

Link for details : https://docs.microsoft.com/fr-fr/windows/wsl/install-win10

### Installing Airflow on Ubuntu WSL

* For the steps to follow, may refer to the scripts inside the directory wsl/

Link for details : https://towardsdatascience.com/run-apache-airflow-on-windows-10-without-docker-3c5754bb98b4

---------------------------------------------------------------------------------------

## Development Environment preparation

### creation de virtualenv

`python -m venv my_venv`

### activation venv

* ne pas oublier de se placer sur le dossier créé (ici ce serait my_venv)

* activer venv sur windows sachant que venv es pour python3 et virtualenv pour python2

`.\my_venv\Scripts\activate`

* pour activer sous linux source

`./bin/activate`

### install requirements (file attached requirements.txt)

`pip install -r requirements.txt`

### print all requirements to a file

`pip freeze >> requirements.txt`

---------------------------------------------------------------------------------------

## Development with airflow

### airflow plugin

https://airflow.apache.org/docs/apache-airflow/1.10.1/plugins.html

### notes

* after how much time a new DAGs should be picked up from the filesystem

> min_file_process_interval = 0
> dag_dir_list_interval = 60

* Note to install and configure awscli (à verifier)

* copy dags from dev to airflow dags

`cp -r /d/review-airflow-wsl/dev/dags/ /home/frils/airflow/`

* copy plugins from dev to airflow plugins (should restart both scheduler and webserver)

`cp -r /d/review-airflow-wsl/dev/plugins/ /home/frils/plugins/`

* S3 operators

https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/s3.html#create-and-delete-amazon-s3-buckets

* dependencies aws providers (for using the s3 operators before)

`pip install 'apache-airflow[amazon]'`

### troubleshooting wsl

https://docs.microsoft.com/fr-fr/windows/wsl/troubleshooting

references
airflow on EKS
https://www.udemy.com/course/apache-airflow-on-aws-eks-the-hands-on-guide/learn/lecture/17777076?src=sac&kw=airflow#overview

complete hands on airflow
https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/13716108#overview

mastering airflow and deploy to kubernetes in AWS
https://www.udemy.com/course/mastering-apache-airflow/learn/lecture/16311008?src=sac&kw=airflow#overview

Develop data in airflow
https://www.udemy.com/course/draft/2145772/learn/lecture/13406176?src=sac&kw=airflow#overview

Apache airflow hands on
https://www.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15809096?src=sac&kw=airflow#overview






