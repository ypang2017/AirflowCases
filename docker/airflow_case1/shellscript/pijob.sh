#! /bin/bash
ssh -Tq localhost << eeooff
                python /home/docker/airflow_case1/pythonscript/pijob.py   
                exit
eeooff
