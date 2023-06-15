# milho-multi-sqlite3-manager

## Description

The idea is to have an environment with multiple SQLITE3 files, aiming at ease of access and use.
The inspiration for creating this module came from the ease of working with Spark in BigData environments where, generally, everything is integrated, without the need to make several explicit connections in the code.

If you want an integrated environment on your machine, create an environment variable called "MULTISQLITE3MANAGER_FOLDER_PATH" with the directory of your folder. You will need to make sure that all files in this folder are SQLITE3 databases.

## Code Samples

```python

from multisqlite3manager import get_connection, print_databases, print_tables
import pandas as pd 

connection = get_connection()
print_databases(connection)
print_tables(connection)


df = pd.read_sql_query("SELECT * FROM db_1.tMisto", connection)
df2 = pd.read_sql_query("SELECT * FROM db_2_copy.tMisto", connection)

```
