import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def hello_world():
    logging.info("Hello World")


def addition():
    logging.info({2+2})


def subtraction():
    logging.info({6-2})


def division():
    logging.info({int(10/2)})


dag = DAG(
    "lesson1.exercise3",
    schedule_interval='*/1 * * * *',
    start_date=datetime.datetime.now() - datetime.timedelta(days=1))

hello_world_task = PythonOperator(
    task_id="hello_world",
    python_callable=hello_world,
    dag=dag)

hello_world_task = PythonOperator(
    task_id = "hello_world",
    python_callable=hello_world,
    dag=dag)


addition_task = PythonOperator(
    task_id="addition",
    python_callable=addition,
    dag=dag)

subtraction_task = PythonOperator(
    task_id ="subtraction",
    python_callable = subtraction,
    dag=dag)


division_task = PythonOperator(
    task_id = "division",
    python_callable = division,
    dag=dag)

hello_world_task >> addition_task
hello_world_task >> subtraction_task
addition_task >> division_task
subtraction_task >> division_task

#
# TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_task
#                   /                 \
#   hello_world_task                   -> division_task
#                   \                 /
#                    ->subtraction_task
