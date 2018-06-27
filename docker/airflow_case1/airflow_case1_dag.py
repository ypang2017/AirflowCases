import airflow,os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

default_args = {
	'owner':'airflow',
	'depends_on_past':False,
	'start_date':airflow.utils.dates.days_ago(1),
	'retries':1,
}

#dag
dag = DAG(
	'airflow_case1_dag',
	default_args=default_args,
	description='airflow_case1 DAG',
	#schedule_interval=timedelta(days=1))
	schedule_interval="30 6 * * *")

#-------------------------------------------------------------------------------
# first operator

init_task_command='''
	/home/docker/airflow_case1/shellscript/init.sh
'''

init_operator = BashOperator(
    task_id='init_task',
    bash_command=init_task_command,
    dag=dag)

#-------------------------------------------------------------------------------
# second operator

mkdir_task_command='''
	/home/docker/airflow_case1/shellscript/mkdir.sh
'''

mkdir_operator = BashOperator(
    task_id='mkdir_task',
    bash_command=mkdir_task_command,
    dag=dag)

#-------------------------------------------------------------------------------
# third operator

put_task_command='''
	/home/docker/airflow_case1/shellscript/put.sh
'''

put_operator = BashOperator(
    task_id='put_task',
    bash_command=put_task_command,
    dag=dag)


#-------------------------------------------------------------------------------
# fourth operator

pi_task_command='''
	/home/docker/airflow_case1/shellscript/pijob.sh
'''

pi_operator = BashOperator(
    task_id='pi_task',
    bash_command=pi_task_command,
    dag=dag)
#-------------------------------------------------------------------------------
# dependencies

init_operator.set_downstream(mkdir_operator)
init_operator.set_downstream(put_operator)
init_operator.set_downstream(pi_operator)
mkdir_operator.set_downstream(put_operator)
put_operator.set_downstream(pi_operator)

