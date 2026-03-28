# Apache Spark

Imagine you had 10TB of log data that needs to compute aggregations daily. If you tried this one machine with something like Pandas, it would likely run out of memory. The solution is to split the work across multiple machines, and Spark let's you do that. Spark will coordinate the computations across different machines to ensure the most efficient processing.

A distributed in-memory computation engine. It takes a computation you describe (i.e., SQL commands), figures out the most efficient execution plan, splits the data across a cluster of machines, executes the statements in parallel, and returns a result.