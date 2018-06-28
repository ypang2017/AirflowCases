# coding:utf-8

import os,sys

def mkdir():
	cmd = "hadoop fs -mkdir -p /docker/airflow_case1/"
	return os.system(cmd)

exit_status = mkdir()

if exit_status == 0:
	sys.exit(0)
else:
	sys.exit(1)

