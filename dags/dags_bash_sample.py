import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_sample",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 2, 10, tz="UTC"),
    catchup=False
) as dag:

    # [START howto_operator_bash]
    t1 = BashOperator(
        task_id="bash_task1",
        bash_command="echo who_am_i",
    )

    t2 = BashOperator(
        task_id="bash_task2",
        bash_command="echo $HOSTNAME",
    )

    t1 >> t2