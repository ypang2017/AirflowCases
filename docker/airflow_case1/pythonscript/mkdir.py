# coding:utf-8

import os,sys

def mkdir():
	cmd = "hadoop fs -mkdir -p /docker/airflow_case1/"
	return os.system(cmd)

mkdir()
