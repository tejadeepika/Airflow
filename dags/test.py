from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="basic_test_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["basic_tests"],
) as dag:
    # Task 1: A simple BashOperator to print a message
    task1 = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello from Task 1!'",
    )

    # Task 2: A simple BashOperator to print a different message
    task2 = BashOperator(
        task_id="print_world",
        bash_command="echo 'Hello from Task 2!'",
    )

    # Set the dependency: Task 1 must run before Task 2
    task1 >> task2