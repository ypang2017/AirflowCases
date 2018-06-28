#! /bin/bash

python /home/docker/airflow_case1/pythonscript/pijob.py
if [ $? -gt 0 ];then
	echo pi job failed!
	exit 1
else
	echo pi job done!
	exit 0
fi
