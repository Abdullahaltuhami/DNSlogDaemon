import os
import sys
from pysql import PySql


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
        print('-')
        print('-')
        print('To start fetching DNSlog Daemon Press 0')
        print('To clean log file press ---- 1:')
        print('To create table in Database press ---- 2:')
        print('To start parssing type ------- start | stop | restart:')
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
            pass
    def op_connection(self):
        pass


if __name__ == '__main__':

    op = start_operation()
    op.ascii_art()
    op.intro()
    if len(sys.argv) == 2:
        if '0' == sys.argv[1]:
            pass
        elif '1' == sys.argv[1]:
            # Run code here
            op.op_one()
        elif '2' == sys.argv[1]:
            # Run code here
            op.op_two()
        elif 'start' == sys.argv[1]:
            os.system('python bin/parser_daemon.py start')
            print('Daemon processed DNS-log')
        elif 'stop' == sys.argv[1]:
            os.system('python bin/parser_daemon.py stop')
            print('Daemon stoped')
        elif 'restart' == sys.argv[1]:
            os.system('python bin/parser_daemon.py restart')
            print('Daemon restarted')
        else:
            print("execute script with either : %s 1|2|start|stop|restart " % sys.argv[0])
            sys.exit(2)
