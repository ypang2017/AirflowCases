# coding:utf-8

import os,sys

def pijob():
	cmd = "hadoop jar /opt/cloudera/parcels/CDH-5.10.2-1.cdh5.10.2.p0.5/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar  pi 10 1"
	return os.system(cmd)

exit_status = pijob()

if exit_status == 0:
	sys.exit(0)
else:
	sys.exit(1)

