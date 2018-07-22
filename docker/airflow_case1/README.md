环境：
操作系统：centos7.2 ，docker
软件版本：airflow 1.8

场景：
在docker中启动airflow，定义一个DAG(airflow_case1),task任务通过ssh免密匙登出docker进入宿主机，
进行CDH集群keytab的init、HDFS文件目录的创建、本地文件上传HDFS及一个mapreduce作业的执行（pi）。

![DAG task执行前](https://github.com/ypang2017/AirflowCases/tree/master/docker/airflow_case1/DAG1.png)

<img src="https://github.com/ypang2017/AirflowCases/tree/master/docker/airflow_case1/DAG1.png" />

![DAG task执行后](https://github.com/ypang2017/AirflowCases/tree/master/docker/airflow_case1/DAG2.png)

<img src="https://github.com/ypang2017/AirflowCases/tree/master/docker/airflow_case1/DAG2.png" />