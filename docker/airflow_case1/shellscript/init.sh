#! /bin/bash

python /home/docker/airflow_case1/pythonscript/init.py
if [ $? -gt 0 ];then
	echo init task failed!
exit 1
else
	echo init task done!
	exit 0
fi
