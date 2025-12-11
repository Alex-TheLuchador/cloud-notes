# Glossary

A comprehensive reference of common cloud and data engineering terminology, organized alphabetically for easy lookup.

## A

### Aggregation
The process of combining multiple rows of data into summary values (e.g., SUM, COUNT, AVG). A fundamental transformation in analytical workloads, typically applied in the [Gold layer](#medallion-architecture) of a data platform.

### Anomaly
A flaw in the design of a relational database schema, typically arising from excessive data redundancy, that causes undesirable consequences or inconsistencies when performing data manipulation operations like inserting, updating, or deleting records. There are three primary types that impact data integrity:
1. Deletion Anomalies
    - Unintentional loss of data when a record is deleted because it was stored with other data that was needed.
2. Insert Anomalies
    - Problems that occur when you cannot insert data without providing other unrelated data.
3. Update Anomalies
    - A data inconsistency that occurs when redundant data is not updated consistently across all its stored locations, leading to conflicting information within the database.

## B

### Batch Processing
Processing data in large, discrete chunks at scheduled intervals (e.g., nightly jobs). Contrasts with [stream processing](#stream-processing). Trade-off: higher latency but simpler to implement and reason about.

## C

### CDC (Change Data Capture)
A pattern for tracking changes in source systems (inserts, updates, deletes) and propagating them downstream. Enables [incremental loading](#incremental-loading) instead of full refreshes.

### Cleaning
The process of identifying and correcting errors, inconsistencies, and inaccuracies in data. Includes handling nulls, removing duplicates, standardizing formats, and correcting typos. Often synonymous with [sanitizing](#sanitizing), though cleaning may imply broader quality improvements beyond just safety/validation. Typically performed in the Bronze-to-Silver transition in [medallion architecture](#medallion-architecture).

## D

### Data Lake
A centralized repository that stores raw data in its native format (structured, semi-structured, or unstructured). Emphasizes storing first, schema-on-read. Common implementations: S3, ADLS, GCS.

### Data Lakehouse
An architecture combining [data lake](#data-lake) storage with [data warehouse](#data-warehouse) capabilities (ACID transactions, schema enforcement, query optimization). Examples: Delta Lake, Apache Iceberg, Apache Hudi.

### Data Lineage
The ability to track data from its origin through transformations to final consumption. Critical for debugging, compliance, and impact analysis.

### Data Warehouse
A structured repository optimized for analytical queries. Enforces schema-on-write, typically uses [dimensional modeling](#dimensional-modeling). Examples: Snowflake, BigQuery, Redshift.

### Deduplication
The process of identifying and removing duplicate records from a dataset. Critical for data quality, especially when consolidating data from multiple sources. Common strategies include keeping first/last occurrence, or merging based on business rules.

### Denormalization
The intentional introduction of redundancy into a data model to improve query performance. Common in [dimensional modeling](#dimensional-modeling) and analytical systems. Trade-off: faster reads, more storage, harder to maintain consistency.

### Dimensional Modeling
A design approach organizing data into facts (measurements/events) and dimensions (descriptive attributes). Optimized for analytical queries and business user comprehension. See also: [star schema](#star-schema), [snowflake schema](#snowflake-schema).

## E

### ELT (Extract, Load, Transform)
Loading raw data first, then transforming it within the target system. Leverages modern warehouse compute power. Contrasts with [ETL](#etl-extract-transform-load).

### ETL (Extract, Transform, Load)
Transforming data before loading into the target system. Traditional approach when target systems had limited compute. Contrasts with [ELT](#elt-extract-load-transform).

### Enrichment
The process of augmenting data with additional context or information from other sources. Examples: adding geographic data based on zip codes, appending customer segments, joining with reference data.

## F

### Filtering
The process of removing rows that don't meet specific criteria. One of the most basic [transformations](#transformation), but critical for reducing data volume and focusing on relevant subsets.

## I

### Idempotency
The property where running an operation multiple times produces the same result as running it once. Critical for reliable data pipelines that may need to retry. Example: `UPDATE table SET status = 'processed'` (idempotent) vs `UPDATE table SET count = count + 1` (not idempotent).

### Incremental Loading
Processing only new or changed data rather than reprocessing everything. Improves efficiency but adds complexity. Often enabled by [CDC](#cdc-change-data-capture) or timestamp-based logic.

## J

### Join
A relational operation combining rows from two or more tables based on related columns. Types include INNER, LEFT, RIGHT, FULL OUTER, and CROSS joins. Performance-critical in [transformation](#transformation) logic.

## M

### Medallion Architecture
A data organization pattern with layers: Bronze (raw), Silver (cleaned/conformed), Gold (aggregated/business-ready). Provides clear separation of concerns. [Cleaning](#cleaning) typically happens Bronze→Silver, [transformation](#transformation) happens Silver→Gold.

### Model Context Protocol (MCP)
MCP is a protocol that allows AI applications to access external 3rd party resources (like Google Drive) and execute tools (like sending emails or running queries). AI applications can use MCP servers that have already been built to connect to 3rd parties, instead of each AI platform developing their own integration and IAM solution.

## N

### Normalization
A database design technique that reduces data redundancy by organizing data into separate related tables. Common in transactional systems. Contrasts with [denormalization](#denormalization) used in analytical systems.

## O

### Orchestration
Coordinating the execution, dependencies, and scheduling of data pipeline tasks. Tools: Airflow, Prefect, Dagster, Mage.

## P

### Partition
Dividing data into smaller, manageable chunks based on a key (often date). Improves query performance and enables efficient [incremental processing](#incremental-loading).

### Pivot
A [transformation](#transformation) that rotates data from rows to columns, converting unique values from one column into multiple columns. Useful for reshaping data for reporting. Inverse operation: [unpivot](#unpivot).

## R

### Resilient Distributed Datasets (RDDs)
Immutable distributed collections of objects that can be processed in parallel. The fundamental data structure in Apache Spark. Lower-level than DataFrames/Datasets.

## S

### Sanitizing
The process of removing or escaping potentially dangerous characters or content from data, particularly to prevent security issues like SQL injection or XSS attacks. Also includes normalizing data to expected formats (e.g., trimming whitespace, standardizing phone numbers). Similar to [cleaning](#cleaning) but with emphasis on safety and validation.

### Schema Evolution
Managing changes to data structure over time while maintaining compatibility. Important for long-lived systems with changing requirements.

### SCD (Slowly Changing Dimension)
Strategies for tracking historical changes in dimension tables:
- **Type 1**: Overwrite (no history)
- **Type 2**: Add new rows with effective dates (full history)
- **Type 3**: Add columns for previous values (limited history)

### Snowflake Schema
A [dimensional modeling](#dimensional-modeling) approach where dimension tables are normalized into multiple related tables. More storage-efficient than [star schema](#star-schema) but potentially slower queries due to additional joins.

### Star Schema
A [dimensional modeling](#dimensional-modeling) approach with a central fact table connected to denormalized dimension tables. Optimized for query performance. Most common analytical schema pattern.

### Stream Processing
Processing data continuously as it arrives, with low latency. Tools: Kafka Streams, Flink, Spark Streaming. Trade-off: more complex than [batch processing](#batch-processing) but enables real-time use cases.

### Surrogate Key
An artificial identifier (typically auto-incrementing integer) used as the primary key instead of natural keys. Provides stability when business keys change. Common in [dimensional modeling](#dimensional-modeling).

## T

### Transformation
The process of converting data from one structure, format, or values to another. Encompasses many operations: [filtering](#filtering), [aggregation](#aggregation), [joins](#join), calculations, type conversions, [pivoting](#pivot), etc. The "T" in [ETL](#etl-extract-transform-load)/[ELT](#elt-extract-load-transform).

### Type Casting
Converting data from one data type to another (e.g., string to integer, timestamp to date). A common [transformation](#transformation) operation that can fail if source data doesn't match expected format.

## U

### Unpivot
A [transformation](#transformation) that converts columns into rows, opposite of [pivot](#pivot). Also called "melting" or "normalizing" wide data into long format.

### Upsert
A database operation that updates a row if it exists, or inserts it if it doesn't. Combines "update" and "insert". Critical for [incremental loading](#incremental-loading) patterns and [CDC](#cdc-change-data-capture) implementations.

## W

### Watermark
A threshold indicating how late data can arrive before being considered too late. Used in [stream processing](#stream-processing) to handle out-of-order events while balancing latency and completeness.

### Window Function
A SQL function that performs calculations across a set of rows related to the current row, without collapsing rows like [aggregation](#aggregation) does. Examples: ROW_NUMBER(), LAG(), LEAD(), running totals. Powerful for analytics and [SCD Type 2](#scd-slowly-changing-dimension) implementations.