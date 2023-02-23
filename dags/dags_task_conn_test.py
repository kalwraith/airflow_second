# Package Import
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id='dags_task_conn_test',
          start_date=datetime(2023,2,16),
          schedule_interval=None,
          catchup=False
) as dag:
    t1 = EmptyOperator(
        task_id='dummy_t1',
    )

    t2 = EmptyOperator(
        task_id='dummy_t2',
    )

    t3 = EmptyOperator(
        task_id='dummy_t3',
    )

    t4 = EmptyOperator(
        task_id='dummy_t4',
    )

    t5 = EmptyOperator(
        task_id='dummy_t5',
    )

    t6 = EmptyOperator(
        task_id='dummy_t6',
    )

    t7 = EmptyOperator(
        task_id='dummy_t7',
    )

    t8 = EmptyOperator(
        task_id='dummy_t8',
    )

