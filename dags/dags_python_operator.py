from airflow import DAG
import datetime
from airflow.operators.python import PythonOperator

def sample_function():
    for i in range(0,10):
        print(i)

with DAG(
    dag_id='dags_python_operator',
    start_date=datetime.datetime(2023,2,20),
    schedule='10 3 * * *',
    catchup=False
) as dag:
    python_task_1 = PythonOperator(
        task_id='python_task_1',
        python_callable=sample_function
    )

    python_task_1