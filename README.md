# milho-multi-sqlite3-manager

## Description

The idea is to have an environment with multiple SQLITE3 files, aiming at ease of access and use.
The inspiration for creating this module came from the ease of working with Spark in BigData environments where, generally, everything is integrated, without the need to make several explicit connections in the code.

If you want an integrated environment on your machine, create an environment variable called "MULTISQLITE3MANAGER_FOLDER_PATH" with the directory of your folder. You will need to make sure that all files in this folder are SQLITE3 databases.

When "from_sql_to_dataframe" is used, the result is a Pandas DataFrame. The query is previously parsed to map all the databases used in the SQL. Then the module create a sqlalchemy connection and attach that databases to the connection. After that, the query is executed and the result is a Pandas DataFrame. 

## Code Samples

```python

import multisqlite3manager.file_manager as fm 
import multisqlite3manager.sqlite3_manager as sm

def log(message: str, log_without_suffix: bool = False):
    print(message) if log_without_suffix else print('>', message)

log('{} {}: {}'.format('Value of enviroment variable', sm.MULTISQLITE3MANAGER_SQLITE_FOLDER_PATH_KEY, sm.MULTISQLITE3MANAGER_SQLITE_FOLDER_PATH_DEFAULT))
log('{} {}: {}'.format('Value of enviroment variable', fm.MULTISQLITE3MANAGER_FILE_MANAGER_ROOT_PATH_KEY, fm.MULTISQLITE3MANAGER_FILE_MANAGER_ROOT_PATH_DEFAULT))

log('Printing the list of sqlite3 databases in the default folder')
sm.print_databases()

log("Printing the list of tables in the database 'teste_3' in the default folder")
sm.print_tables('teste_3')

log('Creating a connection to the database "teste_3" in the default folder')

test_db_conn = sm.create_connection(['teste_3'])

log('test_db_conn: {}'.format(test_db_conn))


stmt = 'select * from teste_3.tMisto UNION ALL select * from teste_4.tMisto'
log('Querying the database "teste_3" and "teste_4" in the default folder')
log('SQL: {}'.format(stmt))

df = sm.from_sql_to_dataframe(stmt)

log(df, True)

```
