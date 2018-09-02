import airflow,os,datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


table_name='test_table'
#yesterday is batch_date
batch_date=(datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':airflow.utils.dates.days_ago(1),
    'retries':1,
}

#dag
dag = DAG(
    'airflow_case2_dag',
    default_args=default_args,
    description='airflow_case2 DAG',
    schedule_interval="30 6 * * *")

#-------------------------------------------------------------------------------
# operator

parameter_test_command='''
	ssh -Tq 192.168.64.129 << eeooff
		/home/docker/airflow_case2/parameter_test.sh %s %s
		exit
eeooff
'''%(table_name,batch_date)

parameter_test_operator = BashOperator(
    task_id='parameter_test',
    bash_command=parameter_test_command,
    dag=dag)

#-------------------------------------------------------------------------------
# dependencies
