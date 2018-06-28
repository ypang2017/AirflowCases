# coding:utf-8

import os,sys

def put():
	#cmd = "hadoop fs -put /home/docker/airflow_case1/pythonscript/test.txt /docker/airflow_case1/"
	cmd = '''
		file_dir=/docker/airflow_case1
		#判断HDFS文件父目录是否存在
		hadoop fs -test -e $file_dir
		if [ $? -eq 0 ];then
			#判断HDFS文件是否存在
			hadoop fs -test -s $file_dir/test.txt
			if [ $? -gt 0 ]; then
				echo start to put the loal file to HDFS
			else
				echo file already exist in HDFS,delete it first
				hadoop fs -rm  $file_dir/test.txt
			fi
		else 
			hadoop fs -mkdir $file_dir
		fi
		hadoop fs -put /home/docker/airflow_case1/pythonscript/test.txt $file_dir
	'''
	return os.system(cmd)

exit_status = put()

if exit_status == 0:
	sys.exit(0)
else:
	sys.exit(1)

