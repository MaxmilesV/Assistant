import pandas as pd
from tabulate import tabulate

program_status = True


def global_command(command, data):
    if command == 'help':
        return print(help_com)
    elif command == 'reset':
        return reset()
    elif command == 'rename':
        return rename(data)
    elif command == 'add data':
        input_value = input('Please type variable name and value.\n'
                            'Input format [var_name value1 value2...]\n'
                            '--> ').split()
        add_var(input_value)
    elif command == 'show data':
        show_var()
    elif command == 'delete data':
        input_value = input('Please type variable name.\n'
                            '--> ')
        del_var(input_value)
    elif command == 'clear data':
        clear_var()
    elif command == 'find data':
        input_value = input('Please type variable name.\n'
                            '--> ')
        find_var(input_value)
    else:
        return print('Sorry, there is no such command.\n'
                     'Type "help" to get command list.\n'
                     'or type "close" to terminate program')


def reset():
    global program_status
    while True:
        agreement = input('Are you sure? (Y/N)\n'
                          '--> ')
        if agreement == 'Y':
            default_data = pd.read_csv('default_data.csv')
            default_data.to_csv('data.csv', index=False)
            default_user_data = pd.read_csv('default_user_storage.csv')
            default_user_data.to_csv('user_storage.csv', index=False)
            print('Done!\n'
                  'Program will automatically close to apply changes')
            program_status = False
            break
        elif agreement == 'N':
            return print('Canceling reset process...')
        print('Please, give a proper answer.')


def rename(data):
    data.loc['name', 'value'] = input('Enter new username.\n'
                                      '--> ')
    print('Done!\n'
          'Now your username is {name}.'.format(
            name=data.loc['name', 'value']))
    data.to_csv('data.csv')


def add_var(data):
    new_data = pd.DataFrame({'variable name': [data[0]],
                             'value': " ".join(data[1:])})
    var_storage = pd.read_csv('user_storage.csv')
    final_data = pd.concat([var_storage, new_data], ignore_index=True)
    final_data.to_csv('user_storage.csv', index=False)
    print('Done!')


def show_var():
    var_storage = pd.read_csv('user_storage.csv')
    var_storage.set_index('variable name')
    print(tabulate(var_storage, headers='keys', tablefmt='psql',
                   showindex=False))


def del_var(input_value):
    var_storage = pd.read_csv('user_storage.csv')
    var_storage.set_index('variable name', inplace=True, drop=True)
    var_storage.drop(index=input_value, inplace=True)
    var_storage.to_csv('user_storage.csv')
    print('Done!')


def clear_var():
    agreement = input('Are you sure? (Y/N)\n'
                      '--> ')
    if agreement == 'Y':
        default_user_data = pd.read_csv('default_user_storage.csv')
        default_user_data.to_csv('user_storage.csv', index=False)
        print('Done!')
    elif agreement == 'N':
        return print('Canceling clearing process...')
    print('Please, give a proper answer.')


def find_var(input_value):
    var_storage = pd.read_csv('user_storage.csv')
    var_storage.set_index('variable name', inplace=True, drop=True)
    print(input_value + ':', var_storage.loc[input_value, 'value'])


help_com = '''<-- GENERAL -->
rename - allows you to enter new username.
close - terminates program.

<-- DATA -->
add data - allows to store data with values separated by space.
delete data - allows to delete data from storage.
find data - allows to find data by name.
show data - prints all stored variables.
clear data - deletes all stored data.

<-- SYSTEM -->
reset - allows you to reset all changes to default value.'''
