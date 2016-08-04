import os
import sys
from pysql import pySql
from parser_daemon import parser_algorithm

class start_operation(object):

    def ascii_art(self):
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

        except Exception as e:
            print(e)
    def intro(self):
        print('-')
        print('-')
        print('To clean log file press 1:')
        print('To create table in Database press 2:')
        print('To start parssing log file to DB execute parser_algorithm with start | stop | restart:')
        print('Log file has to be in one directory where the parser at')
        print('-')
        print('-')


    def op_one(self):
        os.system('sudo chown root:root bin/clean.sh')
        os.system('sudo chmod 700 bin/clean.sh')
        os.system('sudo bin/clean.sh')

    def op_two(self):
        try:
            p = PySql()

            if p.check_table():
                print('table dnslog already exist !!!')
            else:
                p.create_table()
        except Exception as e:
            print(e)


if __name__ == '__main__':

    op = start_operation()
    op.ascii_art()
    op.intro()
    if len(sys.argv) == 2:
        if '1' == sys.argv[1]:
            # Run code here
            op.op_one()
        elif '2' == sys.argv[1]:
            # Run code here
            op.op_two()
        else:
            print("execute script with either : %s 1|2|3 " % sys.argv[0])
            sys.exit(2)
