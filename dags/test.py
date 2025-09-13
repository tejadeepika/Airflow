from __future__ import annotations

import time

from airflow.decorators import dag, task
from datetime import datetime
from airflow.hooks.base import Basehook
from airflow.operators.python import PythonOperator
from wtforms.validators import none_of


def _task_a():
    time.sleep(10)
    print("hello from Teja here..")
    return 42

@dag(
    dag_id="basic_test_dag",
    start_date=datetime(2025, 9, 13, 10),
    schedule='*/1 * * * *',
    catchup=True,
    tags=['task_flow']
)
def task_flow():
    task_a = PythonOperator(
        task_id= 'teja_deepika',
        python_callable=_task_a
    )
    @task
    def task_b(value):
        print("Hello Vishnu")
        print(value)

    task_b(task_a.output)
def stock_market():
    @task.sensor(pokeinterval=30, timeout=300, mode='poke')
    def is_api_available() -> PokeReturnValue:
        import request
        api= Basehook.get_connection('stock_api')
        url = f"{api.host}{api.extra_dejson['endpoint']}"
        print(url)
        response = requests.get(url,headers=api.extra_dejson['headers'])
        condition= response.jsom()['finance']['result']is none
        return PokeReturnValue(is_done=condition, xcom_value=response.json())

    is_api_available()
task_flow()