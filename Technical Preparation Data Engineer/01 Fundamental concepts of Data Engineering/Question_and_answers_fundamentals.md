# Question_and_answers_fundamentals

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

## What is Spark?

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

## 4 What is BigQuery?

BigQuery is Google Cloud’s serverless data warehouse used to store and analyze large amounts of data very quickly using SQL.

Simple explanation:
-------------------

- It can store huge datasets (terabytes, petabytes).
- You run SQL queries on the data.
- It’s very fast because Google handles the computing power behind the scenes.
- It’s serverless, meaning you don’t manage servers — Google does everything.

## 5 what is cloud storage ?

Cloud storage is a service that lets you save data on the internet instead of on your computer or physical hard drive.

Companies like Google Cloud, AWS, and Azure store your files on their servers so you can access them anytime from anywhere.

Simple explanation:
-------------------
- Your data is stored in the cloud (online).
- You don’t need to manage physical hardware.
- It’s secure, scalable, and accessible worldwide.


## 6 what is the diference between dataflow, dataproc and bigquery ?

Dataflow is for serverless data processing, Dataproc is for running Spark/Hadoop clusters, and BigQuery is for fast SQL analytics and warehousing.

### 6.1 Dataflow

- A serverless data processing service in Google Cloud.
- Used for ETL, streaming, and batch processing.
- Based on Apache Beam.
- You don’t manage any clusters — Google handles it.

### 6.2 Dataproc

- A managed Hadoop/Spark cluster on Google Cloud.
- You run Spark, Hive, Hadoop jobs.
- You control the cluster (size, nodes, configs).

### 6.3 BigQuery

- A serverless data warehouse.
- Used for SQL analytics, dashboards, and reporting.
- Runs queries on huge datasets very fast.

