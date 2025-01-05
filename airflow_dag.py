from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'ecommerce_analytics_pipeline',
    default_args=default_args,
    description='E-commerce analytics pipeline with Kafka, Spark, HBase, and Dash',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Task 1: Start Kafka producer
start_kafka_producer = BashOperator(
    task_id='start_kafka_producer',
    bash_command='python /c:/Program Files/BDA/kafka_stream.py',
    dag=dag,
)

# Task 2: Run Spark streaming job
run_spark_streaming = BashOperator(
    task_id='run_spark_streaming',
    bash_command='spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 /c:/Program Files/BDA/spark_stream.py',
    dag=dag,
)

# Task 3: Run Spark HBase integration
run_spark_hbase = BashOperator(
    task_id='run_spark_hbase',
    bash_command='spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.apache.hbase:hbase-spark:2.2.3 /c:/Program Files/BDA/sparkhbaseconnection.py',
    dag=dag,
)

# Task 4: Update Dashboard
update_dashboard = BashOperator(
    task_id='update_dashboard',
    bash_command='python /c:/Program Files/BDA/dashboard.py',
    dag=dag,
)

# Define task dependencies
start_kafka_producer >> run_spark_streaming >> run_spark_hbase >> update_dashboard