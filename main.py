#/usr/bin/env python2
#faisal was here
import sys,time,io
import re
import MySQLdb
import traceback
from daemon import Daemon
from string import digits

class DnslogDaemon(Daemon):
    def run(self):
        # Connection Object
        db = MySQLdb.connect(host='localhost',  user='root',passwd='',db='OGC')
        # ALL queries will be executed witha cursor - cursor object
        cursor = db.cursor()
        start_time = time.time()
        with open('../DNSdebugLog2Clean','r') as f:
            try:
                for line in f.xreadlines():
                    # Clean the lines
                    clean_line = re.split(r'[;,\s]\s*',line)
                    date = clean_line[0]
                    time = clean_line[1]
                    time_con = clean_line[2]
                    UDP_TCP = clean_line[6]
                    snd_rcv = clean_line[7]
                    IP = clean_line[8]
                    # Clean Query & Response incase of one Field Missing
                    if len(clean_line[10]) == 1:
                        # Algorithm flow stays the same
                        QR = clean_line[10]
                    else:
                        # Keep the index clear to stablize the algorithm
                        clean_line.insert(10,'-')
                    if len(clean_line[11]) == 1:
                        # Algorithm flow stays the same
                        QR = QR + '-' + clean_line[11]
                    else:
                        # Keep the index clear to stablize the algorithm
                        clean_line.insert(11,'-')

                    # IF the len is 4 or less then ALgorithm will continue flowing
                        opcode = clean_line[12]

                    if len(clean_line[13]) == 1:
                        opcode = opcode + ' ' + clean_line[13]
                    else:
                        clean_line.insert(13,'-')

                    opcode = opcode + '' + clean_line[14] +' '+clean_line[15]
                    opcode = opcode.replace('[', '').replace(']','')

                    Response_code = clean_line[16]
                    domain = clean_line[17].replace('(', '.').replace(')','').replace('_','-')
                    domain = domain.translate(None,digits)
                            # Insert into table
                    ### TODO
                    cursor.execute('''INSERT INTO dnslog(date,time,time_convention,protocol,snd_rcv,ip,query_response,opcode,domain)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                    (date,time,time_con,UDP_TCP,snd_rcv,IP,opcode,Response_code,domain))
                    db.commit()
                    ### TODO
            except:
                db.rollback()
                traceback.print_exc(file=sys.stdout)
            finally:
                f.close()
                db.close()

if __name__ == '__main__':
    daemon = DnslogDaemon('/tmp/dnsDaemon-OGC.pid')
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
