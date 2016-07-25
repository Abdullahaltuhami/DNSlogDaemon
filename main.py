#/usr/bin/env python3
#faisal was here
import sys,time,io
import re
import MySQLdb
import traceback
from daemon import Daemon
from string import digits


print('Strating script..')
print('daemon initiated')
print('Fetching DNSlogs from remote servers')
print('Fetched DNSlogs from remote servers')
print('Cleaning and importing it to MYSQL Databae')
print('Cleaned and imported it to MYSQL Databae')

class DnslogDaemon(Daemon):
    def run(self):
        # Connection Object
        db = MySQLdb.connect(host='localhost',  user='root',passwd='',db='OGC')
        # ALL queries will be executed witha cursor - cursor object
        cursor = db.cursor()
        start_time = time.time()
        with open('DNSdebugLog2Clean','r') as f:
            try:
                line = f.readline()
                while line:
                    clean_line = re.split(r'[;,\s]\s*',line)
                    domain = clean_line[15].replace('(', '').replace(')','')
                    domain = domain.translate(None,digits)
                    # Insert into table
                    cursor.execute('''INSERT INTO dnslog(Date,Time,Time_convention,Thread_ID,Context,Internal_Packet,UDP_TCP,Send_Receive,Remote_IP,xidhex,Query_Response,opcode,Flags,Response_Code,Question_Type,Question_Name)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(clean_line[0],clean_line[1],clean_line[2],clean_line[3],clean_line[4],clean_line[5],clean_line[6],clean_line[7],clean_line[8],clean_line[9],clean_line[10],clean_line[11],clean_line[12],clean_line[13],clean_line[14],domain))
                    db.commit()
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
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("Usage: %s start|stop|restart " % sys.argv[0])
        sys.exit(2)
