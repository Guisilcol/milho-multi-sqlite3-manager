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

Log output:

```
> Value of enviroment variable MULTISQLITE3MANAGER_SQLITE_FOLDER_PATH: E:\Databases
> Value of enviroment variable MULTISQLITE3MANAGER_FILE_MANAGER_ROOT_PATH: E:\Root File Manager
> Printing the list of sqlite3 databases in the default folder
->  teste_10  -  E:\Databases\teste_10.db
->  teste_10_2  -  E:\Databases\teste_10_2.db
->  teste_3  -  E:\Databases\teste_3.db
->  teste_4  -  E:\Databases\teste_4.db
->  teste_5  -  E:\Databases\teste_5.db
->  teste_6  -  E:\Databases\teste_6.db
->  teste_7  -  E:\Databases\teste_7.db
->  teste_8  -  E:\Databases\teste_8.db
->  teste_8_2  -  E:\Databases\teste_8_2.db
->  teste_9  -  E:\Databases\teste_9.db
->  teste_9_2  -  E:\Databases\teste_9_2.db
->  test_db  -  E:\Databases\test_db.db
->  test_db_2  -  E:\Databases\test_db_2.db
> Printing the list of tables in the database 'teste_3' in the default folder
->  teste_3  -  tTeste
->  teste_3  -  tMisto
->  teste_3  -  tXistoMisto
->  teste_3  -  tXistoLgpdChora
->  teste_3  -  teste
->  teste_3  -  tTesteTabela
> Creating a connection to the database "teste_3" in the default folder
> test_db_conn: <sqlalchemy.engine.base.Connection object at 0x000001E21CA9E990>
> Querying the database "teste_3" and "teste_4" in the default folder
> SQL: select * from teste_3.tMisto UNION ALL select * from teste_4.tMisto
  coluna1 coluna2              coluna3  coluna4
0   milho     gui  2016-10-23 00:00:00        1
1  lukito  kenedo  2016-10-23 00:00:00        2
2   milho     gui  2016-10-23 00:00:00        1
3  lukito  kenedo  2016-10-23 00:00:00        2
```