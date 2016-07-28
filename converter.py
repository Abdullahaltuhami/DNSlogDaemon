#/usr/bin/env python2
# faisal was here
import sys
import time
import re
import MySQLdb
from daemon import Daemon
from string import digits


class DnslogDaemon(Daemon):

    def run():
        # Connection Object
        db = MySQLdb.connect(
            host='localhost',  user='root', passwd='', db='OGC')
        # ALL queries will be executed witha cursor - cursor object
        cursor = db.cursor()
        with open('test', 'r') as f:
            try:
                for line in f.xreadlines():
                    # Clean the lines
                    clean_line = re.split(r'[;,\s]\s*', line)
                    date = clean_line[0]
                    time = clean_line[1]
                    time_con = clean_line[2]
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
                        domain = domain.translate(None, digits)
                        # Insert into table
                        cursor.execute('''INSERT INTO dnslog(date,time,time_convention,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                        (date, time, time_con, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        db.commit()
                    elif len(clean_line) == 18:
                        opcode = clean_line[12]
                        opcode = opcode + ' ' + clean_line[13]
                        opcode = opcode + '' + clean_line[14]
                        opcode = opcode.replace('[', '').replace(']', '')
                        Response_code = clean_line[15]
                        domain = clean_line[16].replace(
                            '(', '.').replace(')', '').replace('_', '-')
                        domain = domain.translate(None, digits)
                        cursor.execute('''INSERT INTO dnslog(date,time,time_convention,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                        (date, time, time_con, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        db.commit()
                    elif len(clean_line) == 17:
                        opcode = clean_line[11]
                        opcode = opcode + ' ' + clean_line[12]
                        opcode = opcode + '' + clean_line[13]
                        opcode = opcode.replace('[', '').replace(']', '')
                        Response_code = clean_line[14]
                        domain = clean_line[15].replace(
                            '(', '.').replace(')', '').replace('_', '-')
                        domain = domain.translate(None, digits)
                        # Insert into table
                        cursor.execute('''INSERT INTO dnslog(date,time,time_convention,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                        (date, time, time_con, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        db.commit()
                    elif len(clean_line) == 16:
                        opcode = clean_line[11]
                        opcode = opcode + ' ' + clean_line[12]
                        opcode = opcode.replace('[', '').replace(']', '')
                        Response_code = clean_line[13]
                        domain = clean_line[14].replace(
                            '(', '.').replace(')', '').replace('_', '-')
                        domain = domain.translate(None, digits)
                        # Insert into table
                        cursor.execute('''INSERT INTO dnslog(date,time,time_convention,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                        (date, time, time_con, UDP_TCP, snd_rcv, IP, opcode, Response_code, domain))
                        db.commit()
                    else:
                        print(clean_line)
                        print(len(clean_line))
            except Exception as e:
                db.rollback()
                print(e)
            finally:
                f.close()
                db.close()

if __name__ == '__main__':
    daemon=DnslogDaemon('/tmp/dnsDaemon-OGC.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
            print('daemon started...')
        elif 'stop' == sys.argv[1]:
            daemon.stop()
            print('daemon stoped...')
        elif 'restart' == sys.argv[1]:
            daemon.restart()
            print('daemon restarted...')
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("Usage: %s start|stop|restart " % sys.argv[0])
        sys.exit(2)
