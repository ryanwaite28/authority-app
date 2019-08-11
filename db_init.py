from chamber import get_connection

sql_file = 'create-tables.sql'
drop_sql_file = 'drop-tables.sql'

def init_tables(drop_tables = False):
    tables_created_count = 0
    try:
        DB = get_connection()
        cursor = DB.cursor()

        if drop_tables == True:
            delete_commands_list = ''
            with open(drop_sql_file) as dfp:
                delete_commands_list = dfp.read().split(';')[:-1]
            
            for command in delete_commands_list:
                try:
                    cursor.execute(command)
                    DB.commit()
                except Exception as e:
                    print('drop command failed:')
                    print(command)
                    raise e

            print('tables dropped successfully')

        commands_list = ''
        with open(sql_file) as fp:
            commands_list = fp.read().split(';')[:-1]

        for command in commands_list:
            try:
                cursor.execute(command)
                DB.commit()
                tables_created_count = tables_created_count + 1
            except Exception as e:
                print('create command failed:')
                print(command)
                raise e

        print('tables created successfully. tables created: ' + str(tables_created_count))

        DB.close()
        print('db closed successfully')

    except Exception as e:
        print('error: could not create tables...')
        print(e)
        if DB:
            print('trying to close db connection...')
            try:
                DB.close()
                print('db closed successfully')
            except Exception as err:
                print('error: could close db...')
                print(err)

init_tables(drop_tables = True)