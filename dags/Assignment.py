from __future__ import annotations

import time

from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator
import random

@dag(
    dag_id= 'random_number_check',
    start_date=datetime(2025, 9, 11),
    schedule='@daily',
    catchup=True,
    tags=['taskflow']
)
def random_number_check():
    @task
    def random_number(**context):
        number=random.randint(1, 100)
        print(f'Generated random number: {number}')

        ti = context['ti']
        ti.xcom_push(key='random', value=number)

    @task
    def check_odd(**context):
        ti = context['ti']
        number = ti.xcom_pull(task_ids='random_number', key='random')
        result ='even' if number % 2 == 0 else 'odd'
        print(f'The number {number} is {result}')

    random_number() >> check_odd()

random_number_check()

