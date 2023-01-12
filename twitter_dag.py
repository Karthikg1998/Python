from airflow import DAG
from datetime import datetime,timedelta
from  airflow.operators.python import PythonOperator
from twitter_etl import twitter_run_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,12,2),
    'email': ['vipinlalkuttan1998@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Twitter_data', default_args=default_args)

PythonOperator(dag=dag,
               task_id='Twitter_data_digging_powered_by_python',
               python_callable=twitter_run_etl,
               )


