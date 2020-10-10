"""
    Airflow w/ Python Operator
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import os
import shutil


def copy_files_to_complete(directory, destination_folder):
    """ This will copy all files in specified directory to complete folder """
    files = os.listdir(directory)

    for f in files:
        if os.path.isfile(os.path.join(directory, f)):
            full_path = os.path.join(directory, destination_folder, f)
            print('Moving file ' + f + ' to ' + destination_folder)
            shutil.move(os.path.join(directory, f), full_path)


def import_file(name):
    """This will import the specified CSV file from the current working directory to stage db"""
    print(name)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['christopher.s.potter@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'copy_files_to_complete',
    default_args=default_args,
    description='Move files from drop directory to complete folder',
    schedule_interval=timedelta(hours=12)
)

task1 = PythonOperator(
    task_id='copy_files_to_complete',
    python_callable=copy_files_to_complete,
    op_kwargs={'directory': '/opt/airflow/data/', 'destination_folder': 'complete'},
    dag=dag
)
