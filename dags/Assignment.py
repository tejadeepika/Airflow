from __future__ import annotations

import time

from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator
import random

@dag(
    dag_id= 'random_number_check',
    start_date=datetime(2025, 9, 13, 10),
    schedule='@daily',
    catchup=False,
    tags=['taskflow']
)
def random_number_check():
    @task
    def random_number():
        number=random.randint(1, 100)
        print('Generated random number: {number}')
        return number
    @task
    def check_odd():
        result ='even' if number % 2 == 0 else 'odd'
        print('The number {number} is {result}')

    check_odd(random_number)
random_number_check()

