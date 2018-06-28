# coding:utf-8

import os,sys

def init():
	cmd1 = "kdestroy;"
	cmd2 = "kinit -kt /opt/cm-5.10.2/run/cloudera-scm-agent/process/520-hdfs-DATANODE/hdfs.keytab hdfs/yuyu01"
	cmd = cmd1 + cmd2
	return os.system(cmd)

exit_status = init()

if exit_status == 0:
	sys.exit(0)
else:
	sys.exit(1)
