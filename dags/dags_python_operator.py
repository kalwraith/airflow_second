from airflow import DAG
import datetime
from airflow.operators.python import PythonOperator

def sample_function(**kwargs):
    for i in range(0,10):
        print(i)
    name_value = kwargs['name']
    address_value = kwargs['address']
    print('name:' + name_value)
    print('address:' + address_value)
    data_interval_start = kwargs['data_interval_start']
    data_interval_end = kwargs['data_interval_end']
    print('data_interval_start:' + str(data_interval_start))
    print('data_interval_end:' + str(data_interval_end))

with DAG(
    dag_id='dags_python_operator',
    start_date=datetime.datetime(2023,2,20),
    schedule='10 3 * * *',
    catchup=False
) as dag:
    python_task_1 = PythonOperator(
        task_id='python_task_1',
        python_callable=sample_function,
        op_kwargs={'name':'hjkim','address':'seoul'}
    )

    python_task_1