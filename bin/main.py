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
        print('-'*60)
        print('-'*60)
        print('Create Tables: press 1')
        print('Give privileges to user: press priv')
        print('Start fetching type fstart | fstop | frestart')
        print('Start parssing type pstart | pstop | prestart:')
        print('-'*60)
        print('-'*60)

    def op_two(self):
        try:
            p = PySql()
            if p.check_table():
                print('Table already exist !!!')
            else:
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
            p = PySql()
            p.create_table()
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
