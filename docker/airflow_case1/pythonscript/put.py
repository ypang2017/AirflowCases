# coding:utf-8

import os

def put():
	cmd = "hadoop fs -put /home/docker/airflow_case1/pythonscript/test.txt /docker/airflow_case1/"
	return os.system(cmd)

put()
