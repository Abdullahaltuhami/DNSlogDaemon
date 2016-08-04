import os
import sys
from pysql import PySql


class start_operation(object):

    def ascii_art(self):
        try:
            print('''

                            88888888ba,   888b      88  ad88888ba
                            88      `"8b  8888b     88 d8"     "8b
                            88        `8b 88 `8b    88 Y8,
                            88         88 88  `8b   88 `Y8aaaaa,
                            88         88 88   `8b  88   `"""""8b,
                            88         8P 88    `8b 88         `8b
                            88      .a8P  88     `8888 Y8a     a8P
                            88888888Y"'   88      `888  "Y88888P"






                            8b,dPPYba,  ,adPPYYba, 8b,dPPYba, ,adPPYba,  ,adPPYba, 8b,dPPYba,
                            88P'    "8a ""     `Y8 88P'   "Y8 I8[    "" a8P_____88 88P'   "Y8
                            88       d8 ,adPPPPP88 88          `"Y8ba,  8PP""""""" 88
                            88b,   ,a8" 88,    ,88 88         aa    ]8I "8b,   ,aa 88
                            88`YbbdP"'  `"8bbdP"Y8 88         `"YbbdP"'  `"Ybbd8"' 88
                            88
                            88                                                                 
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
