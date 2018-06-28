#! /bin/bash

python /home/docker/airflow_case1/pythonscript/mkdir.py
if [ $? -gt 0 ];then
	echo mkdir task failed!
	exit 1
else
	echo mkdir task done!
	exit 0
fi
