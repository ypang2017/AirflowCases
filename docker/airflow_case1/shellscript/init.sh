#! /bin/bash
ssh -Tq localhost << eeooff
	python /home/docker/airflow_case1/pythonscript/init.py
eeooff
echo done!
