import random
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

"""
PythonOperator
- python 함수를 airflow에서 실행할 수 있도록 해주는 오퍼레이터
"""

def random_language():
    language_list = ['PYTHON', 'JAVA', 'RUST']
    language = random.sample(language_list, 1)
    print('SELECTDE LANGUAGE: ', language)

    return language

default_args = dict(
    owner = 'moon',
    email = ['moon@airflow.com'],
    email_on_failure = False,
    retries = 3
)

with DAG (
    dag_id = '02_python_dag',
    start_date = pendulum.datetime(2025, 6, 1, tz='Asia/Seoul'),
    schedule="40 * * * *", # cron 표현식
    tags = ['20251223'],
    default_args = default_args,
    catchup=False
):
    py1 = PythonOperator(
        task_id = 'py1',
        python_callable = random_language
    )

