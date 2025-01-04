# bdapipeline
An elegant BDA pipeline balancing on CAP | kafta, spark, hbase (hdfs), zookeeper, dash (dashboarding), airflow | ecommerce data

### Group: Arbaz Asif, Fazal Ur Rehman, Usman

![Alt text](https://github.com/usmanshafii/bdapipeline/blob/main/pipeline.png)

## BDAPipeline

An elegant Big Data Analytics (BDA) pipeline balancing the CAP theorem using Apache Kafka, PySpark, HBase (with HDFS), Zookeeper, and Airflow for workflow management. This architecture is tailored for e-commerce data processing.

#### implementedarchitecture.jpeg

## Group Members:

### Arbaz Asif

### Fazal Ur Rehman

### Usman Shafi



## Business Problem

E-commerce platforms frequently experience significant, short-term surges in customer activity, such as during events like Black Friday. For instance, U.S. online sales on Black Friday 2024 reached $10.8 billion, marking a 10.2% increase from the previous year. These spikes are not consistent throughout the year, making it inefficient to maintain infrastructure designed for peak traffic at all times.

To address this challenge, there is a need for a scalable architecture that dynamically adjusts to fluctuating demand. This architecture must support:

Real-time data streaming for immediate insights.

Historical data analysis for long-term strategy development.

Our proposed solution ensures robust scalability, cost efficiency, and comprehensive data processing capabilities.

## Data Goals

The primary goal of the pipeline is to achieve:

Real-time Analytics: Ingest and process high-throughput data streams for immediate actionable insights.

Historical Analysis: Enable batch processing and storage for in-depth, long-term analytics.

Scalability: Dynamically adapt to changes in data volume while ensuring fault tolerance and consistency.

## Architecture Design

CAP Theorem Balancing

The proposed pipeline carefully balances the three aspects of the CAP theorem:

### 1. Partition Tolerance (P):

Ensured across the entire pipeline using Kafka’s distributed partitioning, PySpark’s fault tolerance, and HBase’s distributed design.

### 2. Consistency (C):

Achieved in data processing and storage layers with PySpark, HBase, and Zookeeper ensuring synchronized states and deterministic results.

### 3. Availability (A):

Kafka’s distributed architecture ensures high availability, allowing uninterrupted user interaction and resilient message queues.

## Pipeline Components

### Data Extraction

#### Apache Kafka:

Streams data from external sources (e.g., IoT devices, logs, APIs) into PySpark for real-time processing or directly into storage.

### Data Storage

#### Hadoop HDFS:

Distributed storage for large datasets, with processed data archived for historical analysis.

#### Apache HBase:

Provides real-time read/write capabilities for structured data, ensuring fast lookups for dashboards and APIs.

### Real-Time Data Processing

#### PySpark:

Performs real-time data processing for immediate analytics and enrichment.

Supports batch analytics for historical data stored in HDFS.

### Workflow Management

#### Apache Airflow:

Orchestrates data workflows, automating ingestion, transformation, and analytics tasks.

### Visualization and Insights

#### PySpark:

Enables real-time and batch data visualization by generating summarized datasets.

Outputs processed data for use in interactive dashboards or direct business reporting.

## Dataset Overview

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

How the Pipeline Fits Together

## Data Flow:

Ingestion: Kafka streams real-time data from producers (e.g., CSV files, IoT devices) to PySpark or storage layers.

Processing: PySpark processes streamed data for immediate analytics and enriches it for storage in HBase.

## Storage:

HBase stores structured data for low-latency querying.

HDFS archives raw and processed data for batch analysis.

Orchestration: Airflow automates the entire pipeline, managing workflows across components.

Visualization: PySpark-generated summaries provide real-time and batch analytics for interactive dashboards.

Implementation Highlights

## Containerized Environment:

All components, including Kafka, PySpark, HBase, Zookeeper, and Airflow, are containerized using Docker for portability and ease of deployment.

Docker Compose ensures seamless multi-container orchestration.

## Sample Code:

Kafka Producer: Streams CSV data into Kafka topics in real time.

HBase Integration: Stores and queries structured data with PySpark-HBase connectors.

PySpark Analytics: Performs distributed computations for real-time and batch analytics.

## Future Enhancements

Machine Learning Integration:

Predictive modeling for sales forecasting and customer segmentation.

Enhanced Monitoring:

Integrating Prometheus and Grafana for pipeline performance tracking.

Scalable Deployment:

Expanding cloud-based deployment for greater scalability and reliability.

This architecture is designed to address the unique challenges of e-commerce analytics, offering a robust solution for both real-time and historical data needs
Ensure user interactivity even if availability is compromised.

