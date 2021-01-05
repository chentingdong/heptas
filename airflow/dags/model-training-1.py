"""
### Translation Training Pipeline
"""
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "biotranscribe",
    "depends_on_past": False,
    "email": ["tingdong.chen@biotranscribe.com", "steven.xu@biotranscribe.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "Translation model training",
    default_args=default_args,
    description="DAG for training Chinese-English translation model",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["translation"],
)

t1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag,
)

t2 = BashOperator(
    task_id="sleep",
    depends_on_past=False,
    bash_command="sleep 5",
    retries=3,
    dag=dag,
)

# [START documentation]
dag.doc_md = __doc__

t1.doc_md = """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
rendered in the UI's Task Instance Details page.
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
"""
# [END documentation]

# [START jinja_template]
templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id="templated",
    depends_on_past=False,
    bash_command=templated_command,
    params={"my_param": "Parameter I passed in"},
    dag=dag,
)
# [END jinja_template]

t1 >> [t2, t3]
# [END tutorial]