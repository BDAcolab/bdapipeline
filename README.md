# bdapipeline
An elegant BDA pipeline balancing on CAP | kafta, spark, hbase (hdfs), zookeeper, dash (dashboarding), airflow | ecommerce data

### Note: This is a group collaboration project. All rights are reserved by the group members.

## Group Members:

### Arbaz Asif 25251

### Fazal Ur Rehman 24961

### Usman Shafi 25177


![Alt text](https://github.com/usmanshafii/bdapipeline/blob/main/pipeline.png)

## BDAPipeline | Dockerized

An elegant Big Data Analytics (BDA) pipeline balancing the CAP theorem using Apache Kafka, PySpark, HBase (with HDFS), Zookeeper, and Airflow for workflow management. This architecture is tailored for e-commerce data processing.

## Business Problem

E-commerce platforms frequently experience significant, short-term surges in customer activity, such as during events like Black Friday. For instance, U.S. online sales on Black Friday 2024 reached $10.8 billion, marking a 10.2% increase from the previous year. These spikes are not consistent throughout the year, making it inefficient to maintain infrastructure designed for peak traffic at all times.

To address this challenge, there is a need for a scalable architecture that dynamically adjusts to fluctuating demand. This architecture must support:

Real-time data streaming for immediate insights.

Historical data analysis for long-term strategy development.

Our proposed solution ensures robust scalability, cost efficiency, and comprehensive data processing capabilities.

## Overview of the Initial Dataset and Associated Challenges

Our group initially aimed to leverage a real-world dataset to address practical problems and derive meaningful insights through a dashboard. However, we encountered a significant challenge: most of the datasets we found focused on product-related information rather than customer-related orders. This limitation hindered our ability to perform customer-centric analysis and generate actionable queries.

The initial dataset consisted of over 500,000 rows of e-commerce transaction records and provided comprehensive insights into Pakistan's rapidly growing online retail sector. However, when scaled to 1GB (~5 million rows) for big data processing, it introduced several complexities. 
The size of this dataset presented challenges with Kafka ingestion. Despite spending hours, and even days, on ingestion tasks, Kafka could not load the dataset at the consumer side. We eventually decided to work with it in batches, but this approach was still not fully successful.


### Key Challenges
### Data Volume and Scalability

Scaling the dataset to 1GB increased the complexity of real-time streaming and storage.
Efficient management of such a large dataset required significant optimization of resources.
Semi-Structured Nature

The dataset contained varied formats across columns (e.g., text, numeric, and categorical).
Designing a robust schema for storage in HBase was essential to handle this diversity.

### Real-Time Processing Bottlenecks

Streaming the large dataset through Kafka introduced bottlenecks in message consumption.
Issues included network misconfigurations and inefficiencies in data serialization, which impacted throughput.
Resource Constraints

Dockerized services (Kafka, Spark, HBase) faced performance limitations, particularly during parallel processing of large partitions.
Resource allocation and optimization became critical to maintaining pipeline efficiency.

## Dataset
### https://www.kaggle.com/datasets/zusmani/pakistans-largest-ecommerce-dataset

### Dataset Overview

The dataset used for this pipeline is a comprehensive compilation of over half a million e-commerce transactions from Pakistan (March 2016 – August 2018), extended to 1GB for project purposes. Key features include:

Product categories: Fashion, electronics, appliances, etc.

Payment methods: Credit cards, EasyPaisa, Jazz Cash, cash-on-delivery.

Order statuses: Completed, canceled, refunded.

Variables: Item ID, order date, price, quantity, SKU, and customer ID.

This dataset enables analyses like:

Identifying best-selling categories.

Correlating payment methods with order outcomes.

Exploring seasonal trends in customer purchasing behavior.

Predicting order volumes and revenue growth.


## Data Goals

The primary goal of the pipeline is to achieve:

Real-time Analytics: Ingest and process high-throughput data streams for immediate actionable insights.

Historical Analysis: Enable batch processing and storage for in-depth, long-term analytics.

Scalability: Dynamically adapt to changes in data volume while ensuring fault tolerance and consistency.

# Initial Architecture

## Architecture Design

CAP Theorem Balancing

The proposed pipeline carefully balances the three aspects of the CAP theorem:

### 1. Partition Tolerance (P):

Ensured across the entire pipeline using Kafka’s distributed partitioning, PySpark’s fault tolerance, and HBase’s distributed design.

### 2. Consistency (C):

Achieved in data processing and storage layers with PySpark, HBase, and Zookeeper ensuring synchronized states and deterministic results.

### 3. Availability (A):

Kafka’s distributed architecture ensures high availability, allowing uninterrupted user interaction and resilient message queues.

## How the Pipeline Fits Together

### Data Extraction

##### Apache Kafka:

Streams data from external sources (e.g., IoT devices, logs, APIs) into PySpark for real-time processing or directly into storage.

### Data Storage

##### Hbase + HDFS:

HBase stores structured data for low-latency querying and random read write.

HDFS archives raw and processed data for batch analysis.

###### Apache HBase:

Provides real-time read/write capabilities for structured data, ensuring fast lookups for dashboards and APIs.

### Real-Time Data Processing and Insights

##### PySpark:

Performs real-time data processing for immediate analytics and enrichment.

Supports batch analytics for historical data stored in HDFS.

### Workflow Management

##### Apache Airflow:

Orchestrates data workflows, automating ingestion, transformation, and analytics tasks.

## Data Flow:

Ingestion: Kafka streams real-time data from producers (e.g., CSV files, IoT devices) to PySpark or storage layers.

Processing: PySpark processes streamed data for immediate analytics and enriches it for storage in HBase for historical analysis.


# Implemented Architecture

#### Hardware and Software Constraints led us to a halt. Prompting us to think in new ways, and redesign the entire architure

![Alt text](https://github.com/BDAcolab/bdapipeline/blob/main/implementedarchitecture.jpeg) 

## Architecture Design
### Balancing Scalability and Reliability
The implemented pipeline is designed to balance scalability and fault tolerance through containerized solutions:

Scalability: Ensured through Kafka's distributed architecture and Spark's ability to process massive datasets efficiently.
Reliability: Achieved via Docker containerization, providing a stable environment across all stages of the data pipeline.

## Overveiw of the design
### Data Ingestion
##### Apache Kafka:
Kafka ingests the data in real-time, allowing efficient streaming and queuing for downstream processes.
### Data Storage
##### Apache HBase:
HBase stores structured data, supporting real-time read/write operations.
Ensures low-latency querying for real-time dashboards and analytics.
### Data Processing
##### Kafka-Spark and HBase-Spark Connector:
Facilitates seamless integration of Spark with Kafka and HBase for large-scale immediate and historical data processing.
Data Visualization and Analysis
##### PySpark:
Powers the dashboarding and exploratory data analysis (EDA).
Provides insights into processed datasets through visualizations and reports.

# Running the Code:

##### Note: this is not a end to end working project. You will be require to do Troubleshooting on the local machine. 
## Step 1. Clone the Repository
Start by cloning the repository to your local machine:

    ```bash
    git clone https://github.com/username/repo.git
    cd repo
    ```

## 2. Set Up Docker Environment
The entire project is dockerized, so ensure Docker and Docker Compose are installed on your machine. To spin up all the services, navigate to your directory where docker is installed and run the compose command:

    ```bash
    cd 'your directory' #navigate directory
    docker-compose up
    ```
This command will start all the necessary containers, including:

Kafka: For real-time data streaming.
HBase: For data storage and querying.
PySpark: For data processing.
Verify the services are running:

```
bash
docker ps
 ```
## 3. Running Kafka Producer
Kafka ensures that your data is ingested through producers, and consumers maintain the consistency of data flow into the pipeline. However, this part will require you to trouble shoot. 

The Kafka Producer successfully created the topic and sent messages, but the Consumer could not read them due to potential misconfiguration of Kafka advertised listeners in Docker, causing network isolation. Additionally, mismatched consumer group settings or serialization issues with JSON messages may have contributed.



Run the Kafka Producer Script. The Kafka Producer script is pre-configured to stream CSV data into Kafka topics. To run it:

```
bash
python kafka_producer.py
```
The Script Reads the dataset from the data/ directory.
Streams each row as a message to the configured Kafka topic.

### Troubleshooting:
Ensure the advertised.listeners in Kafka are correctly set to match the Docker network, and verify that the consumer's topic, group ID, and deserialization logic align with the producer's configuration. Test connectivity with simple CLI tools to isolate the root cause.



## 4. HBase Integration
The HBase integration is set up to store and query structured data. After the Kafka Producer successfully streams data:

PySpark will write the processed data into HBase.

You can verify the data in HBase using the HBase shell:
```
bash
docker exec -it hbase hbase shell
```
Example to scan a table:

```
bash
scan 'namespace:table_name'
```
## 5. Real-Time Data Processing with PySpark
PySpark is configured to process data in real time using the Kafka-Spark connector. To start the real-time data processing:

```
bash
python pyspark_streaming.py
```
This script:

Connects to the Kafka topic.
Reads and processes incoming messages.
Stores the processed data in HBase.

For batch analytics, run:
```
bash
python pyspark_batch.py
```
## 7. Configuration Details
Make sure the following configurations are aligned with your setup:

Kafka: Verify advertised.listeners in the Docker Compose file matches your network.
HBase: Ensure the schema and table names in the scripts match your requirements.
PySpark: Update any paths or configurations in the .py scripts if necessary.
## 8. Common Troubleshooting Tips
### Kafka Consumer Not Reading Messages:
 
Check if the Kafka topic exists:
```
bash
docker exec -it kafka kafka-topics.sh --list --bootstrap-server localhost:9092
```
Verify advertised.listeners in the Kafka service configuration.

### HBase Connection Issues:

Ensure HBase is running and accessible:
```
bash
docker exec -it hbase hbase shell
```
### PySpark Errors:

Confirm the Spark container can connect to Kafka and HBase services.
By following these steps, you can set up and run the entire pipeline on your local machine seamlessly. The repository includes all the necessary scripts and configurations to get started!

## Containerized Environment:

All components, including Kafka, PySpark, HBase, Zookeeper, and Airflow, are containerized using Docker for portability and ease of deployment.

Docker Compose ensures seamless multi-container orchestration.


# Conclusion
This architecture is designed to address the unique challenges of e-commerce analytics, offering a robust solution for both real-time and historical data needs
Ensure user interactivity even if availability is compromised.

