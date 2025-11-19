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



## to check 

# Apache Airflow Upgrade Guide: 2.2.5 → 3.0

## 📦 Version 2.3.0 (April 30, 2022)
**Key Highlights**
- 🚀 **Dynamic Task Mapping** — generate tasks dynamically based on runtime data.
- 🧭 **Grid View replaces Tree View** in the UI for better observability.
- 🧹 **New CLI commands**
  - `airflow db clean` to purge old metadata.
  - Support for downgrading metadata DB.
- 🗃️ **Database schema changes** — requires migration during upgrade.

---

## ⚙️ Version 3.0.0 (April 22, 2025)
**Major Overhaul**
- 🧩 **Service-Oriented Architecture** — modularized components for scalability.
- 💻 **Modern React-based UI + FastAPI backend** — faster and cleaner web interface.
- 🧾 **DAG Versioning** — immutable DAG snapshots for better auditability.
- 🪄 **Asset-Driven & Event-Based Scheduling** — trigger DAGs when data/assets are available.
- 🌐 **Task Execution API** — execute tasks in multiple environments/languages.
- 🔐 **Enhanced Security** — improved task isolation and authentication mechanisms.
- ☁️ **Hybrid & Multi-Cloud Support** — designed for distributed deployments.

---

## 🧠 Summary
Airflow **3.0** is the biggest evolution since 2.0:
- New architecture for modern data pipelines.
- Cleaner UI and API layers.
- Dynamic, event-driven DAGs.
- Stronger isolation, observability, and scalability.

---

### 🧰 Recommended Actions
1. Review breaking changes in official [Airflow Upgrade Docs](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html).
2. Test DAGs and custom operators in a staging environment.
3. Validate provider package versions.
4. Perform metadata DB migrations with backups.
5. Roll out Airflow 3 gradually in production environments.

datasets/data-driven scheduling (including assets in airflow 3)
event-driven scheduling with assetwatchers
dag bundles 
@asset syntax to define dags
dynamic task mapping
custom xcom backends
async/ deferrable operators
taskflow api/decorators 
object storage feature of the common io provider
setup/teardown tasks 
standalone dag processors 
remote execution 
multiple executor configuration



