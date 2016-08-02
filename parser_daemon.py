#/usr/bin/env python2
import sys, traceback
import time
import re
import MySQLdb
from daemon import Daemon
from datetime import datetime


class parser_algorithm(object):
    def run(self):
        # Connection Object
        db = MySQLdb.connect(
            host='localhost',  user='root', passwd='', db='OGC')
        # ALL queries will be executed witha cursor - cursor object
        cursor = db.cursor()
        # Disable autocommit code mode by siableling
        cursor.execute('''SET autocommit=0;''')
        try:
            with open('../DNSdebugLog2Clean', 'r') as f:
                try:
                    for line in f.xreadlines():
                        # Clean the lines
                        clean_line = re.split(r'[;,\s]\s*', line)

                        date_time = clean_line[0] + ' ' + \
                            clean_line[1] + ' ' + clean_line[2]
                        clean_datetime = datetime.strptime(
                            date_time, '%m/%d/%Y %I:%M:%S %p')

                        UDP_TCP = clean_line[6]
                        snd_rcv = clean_line[7]
                        IP = clean_line[8]
                        QR = clean_line[10]
                        # Case One when line is 19 strings long
                        if len(clean_line) == 19:
                            QR = QR + '-' + clean_line[11]
                            opcode = clean_line[12]
                            opcode = opcode + ' ' + clean_line[13]
                            opcode = opcode + '' + \
                                clean_line[14] + ' ' + clean_line[15]
                            opcode = opcode.replace('[', '').replace(']', '')
                            Response_code = clean_line[16]
                            domain = clean_line[17].replace(
                                '(', '.').replace(')', '').replace('_', '-')
                            # Insert into table

                            cursor.execute('''INSERT INTO dnslog(date_time,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                                           (clean_datetime, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        elif len(clean_line) == 18:
                            opcode = clean_line[12]
                            opcode = opcode + ' ' + clean_line[13]
                            opcode = opcode + '' + clean_line[14]
                            opcode = opcode.replace('[', '').replace(']', '')
                            Response_code = clean_line[15]
                            domain = clean_line[16].replace(
                                '(', '.').replace(')', '').replace('_', '-')
                            cursor.execute('''INSERT INTO dnslog(date_time,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                                           (clean_datetime, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        elif len(clean_line) == 17:
                            opcode = clean_line[11]
                            opcode = opcode + ' ' + clean_line[12]
                            opcode = opcode + '' + clean_line[13]
                            opcode = opcode.replace('[', '').replace(']', '')
                            Response_code = clean_line[14]
                            domain = clean_line[15].replace(
                                '(', '.').replace(')', '').replace('_', '-')
                            # Insert into table
                            cursor.execute('''INSERT INTO dnslog(date_time,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                                           (clean_datetime, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        elif len(clean_line) == 16:
                            opcode = clean_line[11]
                            opcode = opcode + ' ' + clean_line[12]
                            opcode = opcode.replace('[', '').replace(']', '')
                            Response_code = clean_line[13]
                            domain = clean_line[14].replace(
                                '(', '.').replace(')', '').replace('_', '-')
                            # Insert into table
                            cursor.execute('''INSERT INTO dnslog(date_time,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                                           (clean_datetime, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                            db.commit()
                        elif len(clean_line) == 15:
                            print('Debug 15')
                        elif len(clean_line) == 31:
                            print('Debug line with 21')
                        else:
                            print(clean_line)
                            print(len(clean_line))
                except Exception as e:
                    db.rollback()
                    print(e)
                    print('check first Exception')
                    traceback.print_exc(file=sys.stdout)
                finally:
                    db.commit()
                    f.close()
                    db.close()
        except Exception as e:
            print(e)
            print('check first Exception')

class MyDaemon(Daemon):
    def run(self):
        daemon_parser = parser_algorithm()
        daemon_parser.run()


if __name__ == '__main__':
    parser_daemon = MyDaemon('/tmp/OGC-DNS-daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            parser_daemon.start()
            print('daemon started...')
        elif 'stop' == sys.argv[1]:
            parser_daemon.stop()
            print('daemon stoped...')
        elif 'restart' == sys.argv[1]:
            parser_daemon.restart()
            print('daemon restarted...')
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("Usage: %s start|stop|restart " % sys.argv[0])
        sys.exit(2)
