#! /bin/bash
ssh -Tq localhost << eeooff
                python /home/docker/airflow_case1/pythonscript/mkdir.py
                exit
eeooff
echo done!
