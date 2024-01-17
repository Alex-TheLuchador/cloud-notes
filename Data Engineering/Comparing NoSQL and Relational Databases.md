# Comparing NoSQL and Relational Databases

NoSQL and relational databases are both useful, but there may be certain situations in which you'd want to use one over the other. 

By understanding the differences between the two, you can make an informed decision on which is best for your project.

This is NOT a list of all the differences. There are many more to consider, and this list is simply an introdution into their differences.

## 1. Relational database engines enforce strict ACID semantics.
Having consistency in your database is nice, but it can lead to issues with high transactional volues, latency, and availability.
Most relational DBs enforce ACID semantics in order to be consistent. These
restrictions mean you will need to manually shard data, which is time consuming. Distributed DBs
can be a more scalable solution, but maintenance is still an issue.

## 2. Many levels of hierarchy are more easily managed in a NoSQL database.
It will quickly become a burden to manage many parent-child relationships in a
relational database. Document-style NoSQL databases manage deep levels of
hierarchy much better. Refer to the sources for more information.

It's ironic that relational databases are not necessarily that good at modeling
complex relationships. This is because relationships between entities are
calculated at runtime, so operations become very computationally intense as
tihngs grow. Graph database engines treat relationships with higher importance,
which makes graph DBs great for things like managing complex relationships in databases.

## 3. Schema-agnosticism
There are many scenarios in which you may receive data that doesn't conform to the
schema outlined by your relational database. In these scenarios, a NoSQL solutions
can benefit you because they do not need to conform to any specific schema. The data
can be much more fluid and can be adjusted on a per-record basis.

## 4. Strong data consistency
In the event that you do need ensure data is consistent, NoSQL may be difficult to work with.
You would need to sync across all replicas and regions before the data is read,  which means
read times will be longer.

Sources:
- https://learn.microsoft.com/en-us/azure/cosmos-db/relational-nosql