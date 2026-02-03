# Databricks Lakehouse Platform
Databricks Lakehouse aims to improve on the traditional data warehouse and data lake.
- Data warehouses have limitations on unstructured data at scale
- Data lakes traditionally lacked governance

Data lakehouses combine the analytics capabilities of data warehouses with data lake's support of unstructured data and the ability to run data science and ML tasks, all while being easier to govern.

Data lakehouse may not yet be as performant as data warehouses or data lakes, but the platform's maturity (and performance) will increase as time goes on.

## Customer's Databricks Account
### Databricks Control Plane
- Manage workspace notebooks, clusters, and jobs
    - Databricks web app
    - Notebooks
    - Jobs and queries
    - Cluster management
- Starts clusters and jobs running in the Customer's AWS Account.

## Customer's AWS Account
### Classic Compute Plane
- Compute resources for data processing
- Push/pull metadata to Databricks Control Plane

<hr>

# Databricks Architecture
Common workflow:
    1. Data ingested from cloud storage via connectors
    2. Compute starts on-demand
    3. Results of notebooks and jobs are output back to storage
