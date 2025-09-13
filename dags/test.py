from __future__ import annotations

import pendulum

from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator
# with DAG(
#     dag_id="basic_test_dag",
#     start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
#     schedule=None,
#     catchup=False,
#     tags=["basic_tests"],
# ) as dag:
#     # Task 1: A simple BashOperator to print a message
#     task1 = BashOperator(
#         task_id="print_hello",
#         bash_command="echo 'Hello from Task 1!'",
#     )
#
#     # Task 2: A simple BashOperator to print a different message
#     task2 = BashOperator(
#         task_id="print_world",
#         bash_command="echo 'Hello from Task 2!'",
#     )
#
#     # Set the dependency: Task 1 must run before Task 2
#     task1 >> task2

def _task_a():
    print("hello from Teja here..")
    return 42

@dag(
    dag_id="basic_test_dag",
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
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

task_flow()