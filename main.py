import main_command as cd
import sqlite3

# Подключение к БД
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

def main():
    cursor.execute('SELECT state FROM user')
    result = cursor.fetchone()
    if result[0] == 0:
        command = input('Hello, User. How can I help you?\n'
                        'Type "help" for command list.\n'
                        'Or type "close" to terminate program.\n'
                        '--> ')
        cursor.execute('UPDATE user SET state = 1')
        connection.commit()
        cd.main_command(command)
    else:
        cursor.execute('SELECT name FROM user')
        result = cursor.fetchone()
        command = input(f'Hello, {result[0]}. How can I help you?\n'
                        '--> ')
        cd.main_command(command)
    while True:
        command = input('\n--> ')
        cd.main_command(command)

if __name__ == "__main__":
    main()

