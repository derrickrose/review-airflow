from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    "owner": "frils",
    "retries": 1,
}

tags = ["ssh"]

with DAG(
        start_date=datetime(2021, 1, 1),
        description="airflow SSH operator",
        dag_id="ssh_operator",
        dagrun_timeout=timedelta(minutes=60),
        schedule_interval="@daily",
        tags=tags,
        catchup=False,
        default_args=default_args,
        max_active_tasks=100,
        doc_md="""
        to limit up ssh logins per user up to 1, edit the file /etc/security/limits.conf then add line
        [USER]    hard    maxlongins  1
        """
) as dag:
    dummy_task = DummyOperator(task_id="dummy_task", dag=dag)
    ssh_operators = []
    for index in range(100):
        ssh_operator = SSHOperator(
            task_id=f"ssh_operator_{index}",
            ssh_conn_id="miaradia-desktop-01",
            command="cd ~ && ls -l"
        )

        ssh_operators.append(ssh_operator)

    dummy_task >> [*ssh_operators]
