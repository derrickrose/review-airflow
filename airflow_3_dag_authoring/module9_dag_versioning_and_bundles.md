# version and bundles

## why dag versioning ?

- before 3.0 any update to the dag are not versioned
- on the ui if you add new task or delete new task, even the executions of pasts runs for that specific task might
  disappear since airflow assume that the executions were run with the last version of the dag
- no notion of history of changes (except on git)
- worst scenario, dag is running and you make a change so it will be running on the last commit -> error possible
- versioning is a must have for production dag so that you can rollback and of course know under what version of code
  does the dag run

## what is dag versioning ?

- if you dont run a dag after a change, you wont get a new version of the dag
- any structural change is any change that affects serdag (serialization of the data pipeline) (params, task
  dependencies, adding or removing tasks)
- each dag run is associated with a version of the dag
- whenever a new dag run is initiated, the scheduler uses the latest version of the dag to create a run

## dag bundles

- dag versioning is possible thanks to new airflow concept on version 3 dag bundle
- collection of files containing dag code and supporting files.
- named after the backend they use to store the dag code
- there are 2 types of bundles :
    - versioned GitDagBundle remote
    - unversioned as default is the LocalDagBundle (local filesystem)
- clearing and rerunning previous dag run
    - with versioned dag bundle, the scheduler will use the dag version at the time of dag run to create a run, same for
      worker
    - with unversioned dag bundle, the scheduler will use the latest version of the dag to create a run, same for worker
- clearing and rerunning individual tasks of a dag run: same as above
- changing code while a dag is running
    - versioned dag bundle will finish with execution with its current version it has at start
    - unversioned dag bundle will finish with execution with the latest version of the dag
- changing code
    - versioned dag bundle: any structural change will create a new dag bundle version
    - same as unversioned dag bundle
- in production, its recommended to use GitDagBundle
- note it need config and git connection_id , but actually gitsync is obsolete if you use GitDagBundle

## set up you DAG Bundles

- push dag code to the git repo
- install git package in the airflow instance
- install airflow git provider by adding the following apache-airflow-providers-git==<version> to the requirements.txt
- define a git connection using an environment variable
    - to do that use the command export

  ```bash
    export AIRFLOW_CONN_MY_GIT_CONN='
  {
    "conn_type": "git",
    "host": "https://github.com/<account>/<repo>.git",
    "password": "github_pat_<your-token>",
    "git_subdirectory": "dags"
  }'
  ```


- change to make on [dag_processor].dag_bundle_config_list configuration to use the GitDagBundle
- note that the conf waits a list so we can have multiple bundles for example from different git repo
- restart airflow instance to apply the change
  ```bash
    export AIRFLOW__DAG_PROCESSOR__DAG_BUNDLE_CONFIG_LIST='[
  {
    "name": "your-bundle-name",
    "classpath": "airflow.providers.git.bundles.git.GitDagBundle",
    "kwargs":{
        "git_conn_id": "my_git_conn",
        "subdir": "dags",
        "tracking_ref": "main"
    }
  }
  ]'
  ```
- bonus the use of both dag bundle
    ```bash
    export AIRFLOW__DAG_PROCESSOR__DAG_BUNDLE_CONFIG_LIST='[
  {
    "name": "your-bundle-name",
    "classpath": "airflow.providers.git.bundles.git.GitDagBundle",
    "kwargs":{
        "git_conn_id": "my_git_conn",
        "subdir": "dags",
        "tracking_ref": "main"
    }
  }, 
    {
    "name": "dags-folder",
    "classpath": "airflow.providers.git.bundles.git.LocalDagBundle",
    "kwargs":{
        "refresh_interval": 120
    }
  }, 
  
  ]'
  # default refresh_interval is 5 minutes (300 seconds)
  ```