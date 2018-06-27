# coding:utf-8

import os

def init():
	cmd1 = "kdestroy;"
	cmd2 = "kinit -kt /opt/cm-5.10.2/run/cloudera-scm-agent/process/529-hdfs-DATANODE/hdfs.keytab hdfs/yuyu01"
	cmd = cmd1 + cmd2
	return os.system(cmd)

init()
