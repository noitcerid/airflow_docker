"""
    Airflow w/ Python Operator
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import csv
import os
import shutil


def copy_file(source_file, destination_directory='complete'):
    """ This will copy a file from import directory to complete """
    current_directory = '/usr/local/airflow/data/'
    shutil.move(current_directory + source_file, current_directory + destination_directory + '/' + source_file)


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
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'copy_file',
    default_args=default_args,
    description='Move files from drop directory to complete folder',
    schedule_interval=timedelta(hours=1)
)

task1 = PythonOperator(
    task_id='copy_file',
    python_callable=copy_file,
    op_kwargs={'source_file': 'sales_data.csv'},
    dag=dag
)
