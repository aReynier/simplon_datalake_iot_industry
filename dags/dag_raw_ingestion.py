import os
import sys

sys.path.append('/opt/airflow')

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from app.raw.data_ingestion import ingest_data
# from app.raw.data_verification import verify_data_integrity


production_lines = [
    {"id": "A", "name": "LineA_Stable_10K"},
    {"id": "B", "name": "LineB_Flux"},
    {"id": "C", "name": "LineC_Turbulent"},
    {"id": "D", "name": "LineD_SpikeControl"},
    {"id": "E", "name": "LineE_SmoothRun"}
]

def _ingest_raw(line, **context):
    logical_date = context['logical_date']
    year = logical_date.strftime('%Y')
    month = logical_date.strftime('%m')
    
    ingest_data(line, year, month)


with DAG(
    dag_id = 'pipeline_raw_ingestion_v3',
    start_date = datetime(2026, 1, 1),
    schedule = "@daily"
) as dag:
    
    for line in production_lines:

        task_ingest_data = PythonOperator(
            task_id = f"ingest_{line['id']}",
            python_callable = _ingest_raw,
            op_kwargs = {'line': line}
        )

        #As the path change, adapations need to be done for this step
        # task_verify_data_integrity = PythonOperator(
        #     task_id = f"ingest_{line['id']}",
        #     python_callable = verify_data_integrity,
        #     op_kwargs = {'line': line}
        # )

        # task_ingest_data
        # task_ingest_data >> task_verify_data_integrity
