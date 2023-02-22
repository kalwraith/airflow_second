from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=datetime(2022,2,1),
    catchup=False
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo who_am_i",
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo $HOSTNAME",
    )

    task_1 >> task_2

