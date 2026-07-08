# dag_01_hello_world.py

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

# Define the DAG
with DAG(
    dag_id="dag_01_hello_world",      # unique name shown in UI
    start_date=datetime(2024, 1, 1),  # when scheduling starts
    schedule="@daily",                 # run once per day
    catchup=False,                     # don't backfill missed runs
    tags=["beginner"],                 # for filtering in UI
):

    # Define a Python function
    def say_hello():
        print("👋 Hello, Airflow World!")
        print("This is my first DAG task!")

    # Wrap the function in a PythonOperator
    task_hello = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )