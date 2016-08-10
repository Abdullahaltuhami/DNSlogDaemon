import os
import sys
from pysql import PySql
from connection import connect


class start_operation(object):

    def ascii_art(self):
        try:
            print('''
                  __        __
                |/  | /| | /
                |   |( | |(___       ___  ___  ___  ___  ___  ___
                |   )| | )    )     |   )|   )|   )|___ |___)|   )
                |__/ | |/  __/      |__/ |__/||     __/ |__  |
                                    |

                  ''')

        except Exception as e:
            print(e)
            pass

    def intro(self):
        print('')
        print('')
        print('Clean dnslog press: 1')
        print('Create Database & table: press 2')
        print('Give privileges to user: press priv')
        print('Start fetching type fstart | fstop | frestart')
        print('Start parssing type pstart | pstop | prestart:')
        print('-')
        print('-')

    def op_one(self):
        os.system('sudo chown root:root bin/clean.sh')
        os.system('sudo chmod 700 bin/clean.sh')
        os.system('sudo bin/clean.sh')

    def op_two(self):
        try:
            p = PySql()
            if p.check_table() and p.check_database():
                print('Database & table already exist !!!')
            else:
                p.create_database()
                p.create_table()
        except Exception as e:
            print(e)
            pass

    def sudo(slef):
        try:
            p = PySql()
            p.priv()
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    op = start_operation()
    op.ascii_art()
    op.intro()
    if len(sys.argv) == 2:
        if '1' == sys.argv[1]:
            op.op_one()
        elif '2' == sys.argv[1]:
            op.op_two()
        elif 'priv' == sys.argv[1]:
            op.sudo()
        elif 'fstart' == sys.argv[1]:
            os.system('python bin/connection.py start')
        elif 'fstop' == sys.argv[1]:
            os.system('python bin/connection.py stop')
        elif 'frestart' == sys.argv[1]:
            os.system('python bin/connection.py restart')
        elif 'pstart' == sys.argv[1]:
            os.system('python bin/parser_daemon.py start')
        elif 'pstop' == sys.argv[1]:
            os.system('python bin/parser_daemon.py stop')
        elif 'prestart' == sys.argv[1]:
            os.system('python bin/parser_daemon.py restart')
        else:
            print("execute script with either : %s 1|2|start|stop|restart " % sys.argv[0])
            sys.exit(2)
