# bdapipeline
An elegant BDA pipeline balancing on CAP | kafta, spark, hbase (hdfs), zookeeper, dash (dashboarding), airflow | ecommerce data

### Arbaz Asif, Fazal Ur Rehman, Usman

![Alt text](https://github.com/usmanshafii/bdapipeline/blob/main/pipeline.png)

## Data Goal
The main goal is to ensure real-time analytics and historical analytics for high throughput data, entailing consistency, scalability and availability on writes.

## Architecture Design

### CAP Balacing

Partition Tolerance (P) is ensured across the entire pipeline. The pipeline remains operational even when parts of the network are partitioned, thanks to Kafka's partitioning, Spark's fault tolerance, and HBase's distributed nature.

Consistency (C) is prioritized in data processing and storage layers, particularly in Spark, HBase, and Zookeeper. These components ensure deterministic results and synchronized state, critical for data accuracy and reliability.

Availability (A) is handled by Kafka and Dash, which ensure that the system remains functional even when nodes fail. Kafka provides message queues that can continue operating with available brokers, while Dash ensures users can interact with the system even if some backend components experience delays.

Kafka ensures high availability and throughput of data writes, allowing scalability.

Spark is used to ensure the pipeline efficiently processes the data, allowing consistency of storage data and real time analytics.
If a failure occurs, spark's fault tolerance (P) ensures the system recovers and maintains consistency.
 
Hbase ensures fast retrieval with random read/write support, following through on the consistency of storage data and allowing a pretty good dashboarding for historical data.
HDFS's storage and hbase's database model ensures scalability. 

Zookeeper is used to further strengthen consistency and Partition tolerance across Kafka and Hbase.

Dash ensures Quick, personilised dashboarding. Ensuring availability on user interaction. 

Airflow automates the whole process, from data ingestion, processing, storage, and live and historical analytics.


### How the Pipeline Fits

#### Data Extraction
##### Apache Kafka

ROLE: 
Real-time data ingestion from external sources (e.g., IoT devices, APIs, user logs) and distribute real-time data streams to spark. (can also be configured to load data directly into storage)

#### Data Storage
##### Hadoop HDFS

ROLE: 
Distributed storage for large datasets.
Store processed data flushed from hbase for historical analysis or archival.

##### HBase:

ROLE: 
Real-time read/write access. Store real-time, structured data (e.g., time-series or key-value datasets).
Fast lookups for dashboards and APIs.
Leverages HDFS as the storage backend for durability.

#### Real-Time Data Processing
##### Apache Spark

ROLE:
Process data streams from Kafka for real-time analytics.
Enrich data and store results in HBase for low-latency querying.
Perform batch analytics on historical data from HDFS.

#### Workflow Management
##### Apache Airflow

ROLE:
Automate ingestion workflows from Kafka to HDFS.
Schedule Spark jobs for ETL.
Schedule Spark jobs for real-time analytics.
Schedule Spark jobs for periodic batch analytics.
Dashboarding

#### UI
##### Dash
ROLE:
Ensure user interactivity even if availability is compromised.

