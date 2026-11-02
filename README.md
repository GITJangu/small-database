Mini Database

a Mini Database built from scratch, similar to a compilier pipeline. Utilizing SQLGlot for the front end which handles parsing. The catalog, planner, executor, and storage is primarily built by me.

SQLGlot is a SQL parser, transplier, optimizer, and engine. It can be used to format SQL or translate between over 30 dialects. Aims to read a wide variety of SQL Inputs and output syntactically and semantically correct SQL in targeted dialects.


# Architecture

SQL -> SQLGlot -> Logical Planner -> Physical Planner -> Executor -> Storage

| Component | Status |
----------------------
| Front end | Done   |
| Catalog   | Done   |
| Logical Planner | In Progress | 
| Physical Planner | In Progress |
| Executor | In Progress |
| Storage Engine | In Progress |

# Current Working Example

At its current stage, the repo should be able to produce a structured tree based on a SQL query. Which means taking in a raw tree and transforming it into an analyzed tree and developing proper dict values for the logical plan based on the SQL input. 

Example:

Select *
From catalog_test1
Where new_col 1 is not null and new_col1 != 0
Order by new_col 1

Output:

['Select', 'From', 'Where', 'Order', 'And']


# Run It Yourself

pip install -r requirements.txt
python catalog.py

# Current Issues

The idea of the logical plan was that regardless of varying SQL queries, the logical planner would scan the input to develop a hierarchy of the query. Implementation of tree nodes has a bug with node_c not being accessible.
