#import_csv_dag.py

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import csv
import os
import shutil

def copy_file(source_file, destination_directory='complete'):
    """ This will copy a file from import directory to complete """
    current_directory = os.getcwd()
    shutil.move(current_directory + '/' + source_file, current_directory + '/' + source_file)


def import_file(name):
    """This will import the specified CSV file from the current working directory to...?"""
