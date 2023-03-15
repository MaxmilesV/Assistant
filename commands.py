import sqlite3
import sys

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

def rename():
    command = input('Type a new username.\n'
                    'Or type "back" to return to main menu.\n'
                    '--> ')
    if command == 'back':
        print('Returning to main menu...')
        pass
    else:
        cursor.execute(f'UPDATE user SET name = "{command}"')
        connection.commit()
        print('Done!\n'
            f'Now your username is {command}.')

def reset():
    command = input('Are you sure?\n'
                    'Y/N\n'
                    '--> ')
    if command == 'Y':
        cursor.execute('DROP TABLE data')
        connection.commit()
        cursor.execute('CREATE TABLE "data" (data_name TEXT, data_value TEXT)')
        connection.commit()
        cursor.execute('UPDATE user SET name = "User", state = 0')
        connection.commit()
        print('Done!\n'
              'Program will terminate to save changes...\n')
        sys.exit()
    else:
        print('Returning to main menu.')
        pass

def add_data():
    command = input('Enter data name and value in format:\n'
                    'data_name data_value\n'
                    'Or type "back" to return to main menu.\n'
                    '--> ')
    if command == 'back':
        print('Returning to main menu...')
        pass
    else:
        data = command.split()
        cursor.execute(f'INSERT INTO data (data_name, data_value) VALUES ("{data[0]}", "{data[1]}")')
        connection.commit()
        print('Done!')

def delete_data():
    y_n = 'N'
    while y_n == 'N':
        command = input('Enter data name to delete it.\n'
                        'Or type "back" to return to main menu.\n'
                        '--> ')
        if command == 'back':
            return print('Returning to main menu...')
        else:
            y_n = input('Are you sure?\n'
                   'Y/N\n'
                   '--> ')
            if y_n == 'Y':
                cursor.execute(f'DELETE FROM data WHERE data_name = "{command}"')
                connection.commit()
                return print('Done!')

def find_data():
    error = True
    while error:
        command = input('Enter data name your searching for.\n'
                        'Or type "back" to return to main menu.\n'
                        '--> ')
        if command == 'back':
            return print('Returning to main menu...')
        else:
            try:
                cursor.execute(f'SELECT data_value FROM data WHERE data_name = "{command}"')
                result = cursor.fetchone()
                print(f'{command} {result[0]}')
                error = False
            except:
                print('Wrong data name!\n')

def show_data():
    cursor.execute('SELECT * FROM data')
    result = cursor.fetchall()
    for pair in result:
        print(pair[0], pair[1])

def clear_data():
    command = input('Are you sure?\n'
                    'Y/N\n'
                    '--> ')
    if command == 'Y':
        cursor.execute('DROP TABLE data')
        connection.commit()
        cursor.execute('CREATE TABLE "data" (data_name TEXT, data_value TEXT)')
        connection.commit()
        print('All data cleared!')
    else:
        print('Returning to main menu.')
        pass