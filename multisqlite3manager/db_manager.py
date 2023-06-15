import sqlalchemy

MULTISQLITE3MANAGER_FOLDER_PATH_KEY = "MULTISQLITE3MANAGER_FOLDER_PATH"

def get_connection(folder_path: str = None):
    """
        Get a connection to a sqlite3 database file. Attach all other sqlite3 database files in the same folder.
        :param folder_path: The folder path where the sqlite3 database files are located. If None, the environment variable MULTISQLITE3MANAGER_FOLDER_PATH will be used.
        :return: A connection to the sqlite3 database files.
    """
    
    from os import getenv
    from sqlalchemy import create_engine, text
    from glob import glob
    from os.path import basename, splitext

    if folder_path == None and getenv(MULTISQLITE3MANAGER_FOLDER_PATH_KEY) == None:
        raise Exception(f"You must provide a folder path or set the environment variable {MULTISQLITE3MANAGER_FOLDER_PATH_KEY}")
    
    folder = folder_path if folder_path is not None else getenv(MULTISQLITE3MANAGER_FOLDER_PATH_KEY)

    files = glob(f'{folder}/*')

    first_db = None

    if len(files) == 0:
        first_db = f"{folder}/main.db"
    else: 
        first_db = files.pop(0)

    connection = create_engine(f'sqlite:///{first_db}').connect()

    for file in files:
        db_name, _ = splitext(basename(file))
        connection.execute(text(f"ATTACH DATABASE '{file}' AS {db_name}"))

    return connection

def print_databases(connection: sqlalchemy.engine.base.Connection):
    """
        Print all databases attached to the connection.
        :param connection: The connection to the sqlite3 database files.
    """
    from sqlalchemy import text

    result = connection.execute(text("PRAGMA database_list"))
    for row in result:
        _, db_name, path = row
        print('Nome do banco de dados: ', f"'{db_name}'", ' - Diretório: ', f"'{path}'")

def print_tables(connection: sqlalchemy.engine.base.Connection):
    """
        Print all tables in all databases attached to the connection (db_name.table_name).
        :param connection: The connection to the sqlite3 database files.
    """
    from sqlalchemy import text

    result = connection.execute(sqlalchemy.text("PRAGMA database_list"))
    for row in result:
        db_name = row[1]
        tables = connection.execute(text(f"SELECT name FROM {db_name}.sqlite_master WHERE type='table'"))
        for table in tables:
            print(f"{db_name}.{table[0]}")