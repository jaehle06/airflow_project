from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

#dag_id 랑 파일명은 맞추는게 좋음 
with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, # 누락된 구간을 돌리지 않음 True 로 두면 1/1 - 3/1 을 구간을 한꺼번에 돌리므로 문제가 생길 수 있으므로 False로 두는게 좋음
    # tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
        #task는 operator를 통해서 만들어지는거 
        #task id 는 ui에서 graph눌러보면 파랑색 부분 맞춰주기 (객채명 = task id)
        bash_t1 = BashOperator(
            task_id="bash_t1",
            #어떤 쉘 스크립트를 수행할 것이냐? echo = print 랑 비슷
            bash_command="echo whoami",
    )
        bash_t2 = BashOperator(
            task_id="bash_t2",
            #어떤 쉘 스크립트를 수행할 것이냐? echo = print 랑 비슷
            bash_command="echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2