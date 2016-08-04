import os


def star_operation():
    try:
        print('''
  ___  ____   ____ ____      ____  ____  ___
 / _ \|    \ / _  |  _ \    / _  |/ _  |/___)
| |_| | | | ( ( | | | | |  ( ( | ( ( | |___ |
 \___/|_|_|_|\_||_|_| |_|   \_|| |\_||_(___/
                           (_____|


  ____ ___  ____  ____   ____ ____  _   _
 / ___) _ \|    \|  _ \ / _  |  _ \| | | |
( (__| |_| | | | | | | ( ( | | | | | |_| |
 \____)___/|_|_|_| ||_/ \_||_|_| |_|\__  |
                 |_|               (____/
              ''')
        # Scripting start
        print('To clean log file press 1:')
        print('To create table in Database press 2:')
        print('To start parssing log file to DB press 3:')
        print('-')
        print('-')
        print('Log file has to be in one directory where the parser at')
        os.system('./script.sh')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    star_operation()
