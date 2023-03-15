import commands as com
import sys

def main_command(command):
    if command == 'reset':
        com.reset()
    if command == 'help':
        print(help_com)
    if command == 'close':
        print('Terminating program...')
        sys.exit()
    if command == 'rename':
        com.rename()
    if command == 'add data':
        com.add_data()
    if command == 'delete data':
        com.delete_data()
    if command == 'find data':
        com.find_data()
    if command == 'show data':
        com.show_data()
    if command == 'clear data':
        com.clear_data()

help_com = '''<-- GENERAL -->
rename - allows you to enter new username.
close - terminates program.
help - prints this message.

<-- DATA -->
add data - allows to store data with values separated by space.
delete data - allows to delete data from storage.
find data - allows to find data by name.
show data - prints all stored variables.
clear data - deletes all stored data.

<-- SYSTEM -->
reset - allows you to reset all changes to default value.'''
