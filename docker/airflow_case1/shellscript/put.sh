#! /bin/bash

python /home/docker/airflow_case1/pythonscript/put.py
if [ $? -gt 0 ];then
	echo put job failed!
	exit 1
else
	echo put job done!
	exit 0
fi
