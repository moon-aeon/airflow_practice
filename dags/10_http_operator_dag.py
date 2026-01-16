import pendulum, random
from airflow.sdk import DAG, task
from airflow.providers.http.operators.http import HttpOperator
import requests

default_args = dict(
    owner = 'moon',
    email = ['moon@airflow.com'],
    email_on_failure = False,
    retries = 3
)

with DAG(
    dag_id = '10_http_operator_dag',
    start_date = pendulum.datetime(2025, 6, 1, tz='Asia/Seoul'),
    schedule = '30 10 * * *',
    tags = ['20251223'],
    default_args = default_args,
    catchup = False
):
    get_api = HttpOperator(
        task_id = 'get_api',
        http_conn_id = 'brewery_http_conn',
        endpoint = 'v1/breweries',
        method='GET'
    )

get_api