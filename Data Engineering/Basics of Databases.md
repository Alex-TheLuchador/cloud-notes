# The Basics of Databases

## ACID
Most relational DBs enforce ACID semantics in order to be consistent:
- Atomicity
    - An atomic transaction is an indivisible and irreducible set of database operations such that all occurs or nothing occurs - nothing is partial.
- Consistency
    - Ensuring data can be changed only in allowed ways.
- Isolation
    - Lower isolation levels let many users access the same data at once, but at the cost of increasing concurrency effects like dirty reads or lost updates.
    - Higher isolation levels reduces concurrency effects at the cost of system resources and the increased possibility of transactions blocking each other.
- Durability
    - Ensuring changes that have been made are permanent, even in the event of system crashes.