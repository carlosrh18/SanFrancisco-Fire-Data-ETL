from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'carlos',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    dag_id='etl_pipeline',  # ✅ This tells Airflow the name
    default_args=default_args,
    description='A simple ETL pipeline',
    schedule_interval='@daily',
    catchup=False,
    tags=['etl'],
) as dag:

    extract = BashOperator(
        task_id='extract',
        bash_command='python /opt/airflow/scripts/extract.py',
    )

    transform = BashOperator(
        task_id='transform',
        bash_command='python /opt/airflow/scripts/transform.py',
    )

    load = BashOperator(
        task_id='load',
        bash_command='python /opt/airflow/scripts/load.py',
    )

    extract >> transform >> load