import commands as cd
import pandas as pd

data = pd.read_csv('data.csv')
data.set_index('var', inplace=True, drop=True)

if data.loc['new_user', 'value'] == 'True':
    command = input('Hello, User. How can I help you?\n'
                    'Type "help" for command list.\n'
                    'Or type "close" to terminate program.\n'
                    '--> ')
    data.loc['new_user', 'value'] = 'False'
    data.to_csv('data.csv')
else:
    command = input('Hello, {name}. How can I help you?\n'
                    '--> '.format(name=data.loc['name', 'value']))

while True:
    if command.lower() == 'close':
        break
    else:
        cd.global_command(command, data)
        executing = cd.program_status
        if not executing:
            break
    command = input('--> ')
