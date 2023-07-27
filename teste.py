


def main():
    print('> Módulos reconhecidos pela função find_packages():')
    from setuptools import find_packages
    print(find_packages())

    print('> Módulo importado:')
    import multisqlite3manager
    print(multisqlite3manager)
    print(multisqlite3manager.sqlite3_manager.create_connection)



if __name__ == '__main__':
    main()