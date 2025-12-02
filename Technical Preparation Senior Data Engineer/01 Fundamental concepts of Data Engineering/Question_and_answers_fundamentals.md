# QUESTION_AND_ANSWERS_FUNDAMENTALS_GENERAL

## 0 What is python?

Python is a typed language, but it uses dynamic typing, meaning you don’t have to declare variable types — Python figures them out at runtime.

### 0.1 There are immutable and mutable objects — what are they?

In Python, some objects are mutable and some are immutable.

Immutable objects:
------------------
- Their value cannot change after they are created.
- Examples: int, float, string, tuple, bool

Mutable objects:
----------------
- Their value can change after they are created.
- Examples: list, dict, set

Simple difference:
------------------
- Immutable = you can’t modify the object itself
(if you “change” it, Python creates a new object)

- Mutable = you can modify the object in place
(no new object is created)

### 0.2 What is a function?

A function is a reusable block of code that takes input, performs some logic, and returns an output.

## 1 What is SQL?

SQL is a language used to store, retrieve, and manage data in relational databases. It lets you query data, update it, and organize it using tables.

### 1.2 What is the difference between DDL(Data Definition Language) and DML(Data Manipulation Language)

#### DDL – Data Definition Language
Used to define or change the structure of database objects (tables, views, schemas).

Examples:
---------
- CREATE
- ALTER
- DROP
- TRUNCATE

#### DML – Data Manipulation Language
Used to work with the data inside those structures.

Examples:
---------
- SELECT
- INSERT
- UPDATE
- DELETE

### 1.3 What is an agregation ?
An aggregation (in SQL or data engineering) is an operation that combines multiple rows into a single result by applying a function.

Common aggregation functions:
-----------------------------
- SUM() → adds values
- COUNT() → counts rows
- AVG() → average
- MAX() / MIN() → highest or lowest value

### 1.4 There another type of operations , which ones ?

Filtering
---------
- Select only the rows you want.
- Uses: WHERE, HAVING

Joins
-----
- Combine data from multiple tables.
- Types: INNER, LEFT, RIGHT, FULL

Sorting
-------
- Order the results.
- Uses: ORDER BY

Grouping
--------
- Group rows so you can apply aggregations.
- Uses: GROUP BY


Window Functions
----------------
- Calculations across a set of rows without reducing row count.
- Uses: OVER()

Set Operations
--------------
- Combine query results.
- UNION
- UNION ALL
- INTERSECT
- EXCEPT

Subqueries
----------
Queries inside other queries.

SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);


## 1 What is the diference betwen a delta lake and data lake ?

- A Data Lake is just a big place to store all kinds of data (raw, structured, unstructured).It’s cheap and flexible, but it doesn’t guarantee data quality or organization.

- A Delta Lake is basically an improved version of a data lake.It sits on top of the data lake and adds 
useful features like:

- ACID transactions (so data isn’t corrupted)
- Version control / time travel (you can see or restore old data)
- Schema checks (avoid bad data)
- Easy updates and deletes

Simple analogy:
---------------
- A data lake is like a big storage room where you can put anything.
- A Delta Lake is that same room but with organization, labels, security, and a tracking system so you know what changed and when.

## 2 What is Spark?

Apache Spark is a fast, open-source framework used to process large amounts of data across many machines.

Simple explanation:
-------------------
- It allows you to work with big data that can’t fit on one computer.
- It processes data in parallel, which makes it very fast.
- It can work with batch data, real-time streams, SQL, machine learning, and graph processing.

Why is Spark popular?
---------------------
- It’s much faster than older technologies like Hadoop MapReduce (uses in-memory processing).
- It’s easy to program using Python, SQL, Scala, or Java.
- It scales from one laptop to thousands of servers.

## 3 What is a RDD ?

An RDD (Resilient Distributed Dataset) is the basic data structure in Apache Spark.
It represents a fault-tolerant collection of data that is split across many machines so it can be processed in parallel.

Simple explanation:
-------------------

- It’s Spark’s core data structure.
- It is immutable (you can’t change it once created; you create a new one).
- It works in memory, making it fast.
- It’s distributed, so chunks of data run on multiple computers.
- It can recover automatically if part of the data is lost (because of lineage).

### 3.1 What is the difference between RDD and DataFrame ?

Simple Answer
-------------
- RDD is the low-level, raw distributed data structure in Spark.
- DataFrames are a higher-level abstraction built on top of RDDs with schema, column operations, and automatic optimization, making them easier and faster to use.

RDD (Resilient Distributed Dataset)
-----------------------------------
- Low-level data structure in Spark.
- You control everything (types, operations, logic).
- No built-in optimization — you must manage performance.
- Good for complex, unstructured data or when you need full control.

DataFrame
---------
- Higher-level data structure (like a table).
- Easier to use: you work with columns instead of low-level code.
- Spark automatically optimizes it using Catalyst optimizer.
- Faster than RDD for most jobs.
- Good for structured data (rows & columns).

## 4 What is Apache Kafka ?

Apache Kafka is a distributed streaming platform used to move data between systems in real time.

Simple explanation:
-------------------
- It lets different systems send messages (producers)
- And other systems read those messages (consumers)
- Messages are stored in topics
- Kafka keeps data in order, durable, and highly scalable
- Think of Kafka like a high-speed, fault-tolerant “data bus” that connects all parts of your data ecosystem.

Used for:
---------
- real-time data pipelines
- event-driven systems
- log/metric streaming
- microservices communication
- ETL streaming

### 4.1 How its works? 

How Kafka Works (Step-by-Step)
------------------------------

#### Producers send messages
- A producer is any application that writes data to Kafka.

Example:
--------
- A service sends “new order placed” events to a Kafka topic called orders.

#### Kafka stores messages in topics
- A topic is like a folder or stream where messages are kept.
- Each topic is split into partitions (like lanes on a highway) so Kafka can scale and write very fast.
- Kafka stores messages durably on disk and keeps them for a configured time (hours, days, weeks).

#### Consumers read messages
- A consumer is any application that reads data from Kafka.

Example:
--------
- A fraud detection service reads the orders topic to analyze new orders.
- Consumers read messages in order within each partition.

#### Consumer groups allow scaling
- Multiple consumers can work together in a consumer group.
- Kafka will balance partitions across consumers so you can process more data in parallel.

#### Kafka keeps track of offsets
- Each message has an offset (its position).
- Consumers track which offset they’ve read so they can:
- stop and restart
- resume from the last processed message
- or reprocess messages if needed

#### In short

Kafka works like this:
----------------------
- Producer → Topic/Partitions → Consumer Group.

##### Kafka guarantees:
- High throughput
- Durability
- Scalability
- Ordered messages (per partition)
- Fault tolerance

### 4.2 What are the difference between Kafka and Pub/Sub
- Yes — Kafka is similar to Pub/Sub, but with some important differences.

How Kafka is like Pub/Sub → **Amazon SNS (Simple Notification Service)**:
--------------------------
- Producers publish messages to topics
- Consumers subscribe to those topics
- Messages flow from publishers → subscribers
- So at a high level, yes, it works like a pub/sub system.

But Kafka is more powerful than classic Pub/Sub

Here are the key differences:
-----------------------------

-- Kafka stores messages on disk1
-- In traditional pub/sub (like RabbitMQ), messages are gone once delivered.
-- In Kafka, messages are stored for hours, days, or weeks — even after they’re consumed.

# QUESTION_AND_ANSWERS_FUNDAMENTALS_GCP

## 0 What is BigQuery?

BigQuery is Google Cloud’s serverless data warehouse used to store and analyze large amounts of data very quickly using SQL.

Simple explanation:
-------------------

- It can store huge datasets (terabytes, petabytes).
- You run SQL queries on the data.
- It’s very fast because Google handles the computing power behind the scenes.
- It’s serverless, meaning you don’t manage servers — Google does everything.

## 1 What is Cloud Composer?

Cloud Composer is Google Cloud’s managed version of Apache Airflow.

It lets you create, schedule, and monitor workflows (pipelines) without having to install or manage Airflow yourself.

With Airflow you can:
---------------------

- Build pipelines defined as DAGs (Directed Acyclic Graphs)
- Schedule tasks (daily, hourly, etc.)
- Run tasks in order with dependencies
- Retry failed tasks
- Orchestrate multiple systems (BigQuery, Dataflow, Dataproc, GCS, APIs, etc.)
- Monitor and manage workflows from a web UI

## 2 what is cloud storage ?

Cloud storage is a service that lets you save data on the internet instead of on your computer or physical hard drive.

Companies like Google Cloud, AWS, and Azure store your files on their servers so you can access them anytime from anywhere.

Simple explanation:
-------------------
- Your data is stored in the cloud (online).
- You don’t need to manage physical hardware.
- It’s secure, scalable, and accessible worldwide.

## 3 What is Cloud Run?

Cloud Run is a Google Cloud service that lets you run containerized applications (Docker containers) in a serverless way.

This means:

- You don’t manage servers
- Your app scales automatically
- You only pay when it’s running


What can you run on Cloud Run?
------------------------------

- APIs
- Web apps
- Microservices
- Backend services
- Background jobs
- Anything that can run in a container

## 4 What is Secret Manager?

Secret Manager lets you save your secrets in the cloud safely and access them only when needed, with proper permissions.

Simple explanation:
-------------------
Secret Manager is a service used to store and protect sensitive information such as:

- passwords
- API keys
- tokens
- certificates
- database credentials

## 5 ¿Qué es IAM? (Identity and Access Management)

IAM is the system that controls who can access what in a cloud environment.
It manages:

- Users
- Roles
- Permissions
- Service accounts (identities for apps)

## 6 What is Bigtable?

Bigtable is Google Cloud’s NoSQL database designed to handle very large amounts of data with low latency and high performance.

What Bigtable is good for:
--------------------------

- Time-series data
- IoT data
- Financial data (stock prices, logs)
- Recommendation systems
- Analytics needing fast lookups

## 7 What is Cloud Spanner?

Cloud Spanner is Google Cloud’s fully managed, globally scalable SQL database.

Cloud Spanner is a SQL database that can scale to huge sizes, even across multiple regions, without losing consistency.

When it's used:
---------------

- Financial apps
- Global e-commerce systems
- Inventory systems
- Gaming backends
- Applications needing strong consistency and high scale

## 8 what is the diference between dataflow, dataproc and bigquery ?

Dataflow is for serverless data processing, Dataproc is for running Spark/Hadoop clusters, and BigQuery is for fast SQL analytics and warehousing.

### 8.1 Dataflow

- A serverless data processing service in Google Cloud.
- Used for ETL, streaming, and batch processing.
- Based on Apache Beam.
- You don’t manage any clusters — Google handles it.

### 8.2 Dataproc

- A managed Hadoop/Spark cluster on Google Cloud.
- You run Spark, Hive, Hadoop jobs.
- You control the cluster (size, nodes, configs).

### 8.3 BigQuery

- A serverless data warehouse.
- Used for SQL analytics, dashboards, and reporting.
- Runs queries on huge datasets very fast.


# QUESTION_AND_ANSWERS_FUNDAMENTALS_AWS

## 0 What is BigQuery? → **Amazon Redshift**

**Amazon Redshift** is AWS’s cloud data warehouse used to store and analyze massive datasets with SQL.

**Simple explanation:**
-----------------------

* Stores huge datasets (TBs–PBs)
* Run fast SQL queries
* Fully managed (no servers)
* Integrates with AWS analytics tools
* Scales compute and storage


## 1 What is Cloud Composer? → **Amazon MWAA (Managed Workflows for Apache Airflow)**

**Amazon MWAA** is AWS’s managed Apache Airflow service.

**With Airflow you can:**
-------------------------

* Build pipelines as DAGs
* Schedule tasks
* Define dependencies
* Retry failures
* Orchestrate AWS services (Redshift, Glue, EMR, S3, Lambda, etc.)
* Monitor workflows from a UI


## 2 What is Cloud Storage? → **Amazon S3**

**Amazon S3** is AWS’s cloud object storage service.

**Simple explanation:**
-----------------------

* Store files in the cloud
* No hardware needed
* Secure and scalable
* Accessible from anywhere
* Used for backups, data lakes, analytics


## 3 What is Cloud Run? → **AWS Fargate / AWS Lambda**

Cloud Run runs serverless containers.
AWS equivalents:

### **AWS Fargate**

* Serverless containers
* No servers to manage
* Auto-scaling
* Pay only when running

### **AWS Lambda**

* Serverless functions
* Auto-scaling
* Pay per request

**What you can run:**

* APIs
* Web apps
* Microservices
* Background jobs
* Any Docker container (via Fargate)

## 4 What is Secret Manager? → **AWS Secrets Manager**

**AWS Secrets Manager** securely stores sensitive information such as:

* Passwords
* API keys
* Tokens
* Database credentials
* Certificates

Supports automatic secret rotation.

## 5 What is IAM? → **AWS IAM (Identity and Access Management)**

IAM manages permissions and identity access across AWS.

**IAM controls:**

* Users
* Roles
* Permissions
* Security policies
* Role-based access for services (Lambda, EC2, ECS, etc.)

## 6 What is Bigtable? → **Amazon DynamoDB**

**Amazon DynamoDB** is AWS’s high-performance NoSQL database.

**Best for:**

* Time-series data
* IoT sensor data
* Financial/log data
* Recommendation systems
* Low-latency lookups
* Real-time analytics

Fully serverless and scalable.

## 7 What is Cloud Spanner? → **Amazon Aurora (Global Database)** / **DynamoDB Global Tables**

Google Cloud Spanner is a globally scalable SQL database.

**AWS equivalents:**

### **Amazon Aurora Global Database**

* Fully managed relational SQL
* Global replication
* Strong consistency

### **DynamoDB Global Tables**

* Fully managed NoSQL
* Multi-region replication
* Global scale

Closest match = **Aurora Global Database**.

**Use cases:**

* Financial systems
* E-commerce
* Inventory systems
* Global user apps


## 8 Dataflow vs Dataproc vs BigQuery → AWS equivalents

**Dataflow** <=> **AWS Glue / Kinesis Data Analytics** <=> Serverless data processing(ETL,batch,streaming)
**Dataproc** <=>           **Amazon EMR**              <=> Managed Hadoop/Spark clusters
**BigQuery** <=>         **Amazon Redshift**           <=> Serverless cloud data warehous

## 8.1 Dataflow → **AWS Glue / Kinesis Data Analytics**

* Serverless ETL pipelines
* Streaming & batch processing
* No clusters to manage
* Glue = Apache Spark
* Kinesis = streaming SQL

## 8.2 Dataproc → **Amazon EMR**

* Managed Hadoop/Spark clusters
* Highly customizable
* Runs Spark, Hive, Hadoop jobs

## 8.3 BigQuery → **Amazon Redshift**

* Serverless Redshift Serverless available
* Fast SQL analytics
* Ideal for BI, dashboards, data warehousing



## 7 Have you been working with on-premise servers in Spark or just in the cloud?

- I have experience working with Spark in both on-premise environments and in the cloud.
On-premise, I’ve worked with Hadoop/YARN-based Spark clusters, handling resource management, cluster configuration, and job performance tuning.

- In the cloud, I’ve used managed services like Dataproc (GCP) and EMR (AWS), which simplify cluster setup and scaling.

- Overall, I’m comfortable with both environments and understand the differences in deployment, optimization, and cost management.

## 7.1 Have you worked with enterprise databases like Oracle or SQL Server?

- I have managed both Oracle and SQL Server instances supporting transactional workloads and downstream analytics, handling schema design, performance tuning, and backup/restore strategies.
- With Oracle, I’ve implemented PL/SQL-based ETL routines, configured partitioning, and integrated GoldenGate/CDC feeds to land data in cloud storage.
- With SQL Server, I’ve optimized SSIS packages, set up Always On availability groups, and exposed data via views or stored procedures consumed by Spark and BI tools.
- I’ve also built ingestion patterns that replicate data from these databases into modern data lakes/warehouses using connectors such as Datastream, AWS DMS, or Debezium.

## 7.2 How have you used serverless functions (e.g., Cloud Functions, AWS Lambda) in data engineering workflows?

- I leverage serverless functions for lightweight, event-driven tasks like schema validation, metadata enrichment, and triggering downstream jobs whenever new files arrive in storage.
- They serve as glue code that connects services: reading from Pub/Sub/SQS topics, calling REST APIs, or invoking Dataproc/Spark jobs as part of a larger pipeline.
- I implement observability (structured logging, metrics, dead-letter queues) and guardrails such as idempotency keys and retries to keep these functions production-ready.
- Serverless functions help keep costs low and simplify operations because there are no servers to manage, yet they scale instantly with the volume of events.

## 7.3 What orchestration tools have you used to coordinate data workflows?

- I design and maintain DAGs in Apache Airflow/Cloud Composer, orchestrating batch and streaming jobs across BigQuery, Dataproc, and on-prem systems.
- I’ve also worked with AWS Step Functions and Azure Data Factory for event-driven pipelines, leveraging native integrations with Lambda, Glue, and Synapse.
- My workflows include automated dependency management, SLA monitoring, and alerting integrations (Slack, PagerDuty) to ensure timely responses.
- I apply best practices such as parametrized DAGs, dynamic task mapping, and modular operators so pipelines remain maintainable and reusable across projects.
