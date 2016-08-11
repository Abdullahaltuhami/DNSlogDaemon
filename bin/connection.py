#!/usr/bin/env python
import os
import sys
import traceback
import glob
from daemon import Daemon
from operator import add
import MySQLdb
import time

class connect(object):

    def set_connection(self):
        try:
            if not os.path.isdir('/home/rwx/Desktop/winshare'):
                os.system('sudo mkdir -p /home/rwx/Desktop/winshare')
                os.system(
                    'sudo mount.cifs //192.168.15.158/c$ /home/rwx/Desktop/winshare -o user=abdullah.altuhami,domain=oman-gas,password=@bdull@h_94')
            else:
                pass

        except Exception as e:
            print("Exception:")
            print('-'*60)
            traceback.print_exc(file=sys.stdout)
            print('-'*60)

    def create_dirs(self):
        if not os.path.isdir('/home/rwx/Desktop/parsing2DB/notclean'):
            os.system('sudo mkdir -p /home/rwx/Desktop/parsing2DB/notclean')
        else:
            pass

        if not os.path.isdir('/home/rwx/Desktop/parsing2DB/clean'):
            os.system('sudo mkdir -p /home/rwx/Desktop/parsing2DB/clean')
        else:
            pass


class fetcher(Daemon):
    host_name = 'localhost'
    user_name = 'root'
    passwd = 'rootserver'
    db_schema = 'OGC'
    the_file_path =''

    def run(self):
        try:
            db = MySQLdb.connect(host=self.host_name,user=self.user_name, passwd=self.passwd, db=self.db_schema)
            cursor = db.cursor()

            #cp_from = '/home/rwx/Desktop/winshare/Users/abdullah.altuhami/Documents'
            cp_from = '/home/rwx/Documents'
            cp_to = '/home/rwx/Desktop/parsing2DB/notclean'

            for path_from in glob.glob(cp_from + '/ogc*'):
                self.the_file_path = path_from

            creation_date = time.ctime(os.path.getctime(self.the_file_path))
            # If Table is empty copy anyway

            row_count = cursor.execute(''' SELECT COUNT(*) FROM information_schema.TABLES WHERE table_name = 'fetchlog' ''')
            # If database is not empty
            if row_count > 0:
                cursor.execute('''SELECT creation FROM OGC.fetchlog order by id DESC limit 1''')
                result = cursor.fetchall()
                result_clean = ''.join(elem[0] for elem in result)
            else:
                cursor.execute('''INSERT INTO fetchlog(creation)VALUES(%s)''',[creation_date])
                db.commit()
                cursor.execute('''SELECT creation FROM OGC.fetchlog order by id DESC limit 1''')
                result = cursor.fetchall()
                result_clean = ''.join(elem[0] for elem in result)
                # Not equal means new File was created by server
            if result_clean != creation_date:
                # If file is new and bigger than 498 MB -- > 513802240 bytes
                if os.path.getsize(self.the_file_path) >= 13107200:
                    # Log new This file into database
                    cursor.execute('''INSERT INTO fetchlog(creation)VALUES(%s)''',
                                   [creation_date])
                    db.commit()

                    # add creation timestamp to file
                    for path_from in glob.glob(cp_from + '/ogc*'):
                        cmd = '{0} {1} {2}'.format('sudo cp', path_from, cp_to)

                    # Copy it to parsing2DB
                    os.system(cmd)

                    # Clean it fpr parsing2DB
                    # Now it will be clean
                    os.system('sudo chown root:root bin/clean.sh')
                    os.system('sudo chmod 700 bin/clean.sh')
                    os.system('sudo bin/clean.sh {0} {1}'.format(self.the_file_path,'/home/rwx/Desktop/parsing2DB/clean/dnslogclean'))
                else:
                    print('Something was passed at file size MB checked')
                    pass
            else:
                print('Something was passed at creation time check ---- yoyoyoyoyoyoyo')
                pass

        except:
            print("Exception:")
            print('-'*60)
            traceback.print_exc(file=sys.stdout)
            print('-'*60)


if __name__ == '__main__':
    try:
        fetch = fetcher('/tmp/OGC-fetcher-daemon.pid')
        con = connect()
        con.set_connection()
        con.create_dirs()

        if len(sys.argv) == 2:
            if 'start' == sys.argv[1]:
                    # Use .run instead of .start to debug your code
                fetch.run()
            elif 'stop' == sys.argv[1]:
                fetch.stop()
            elif 'restart' == sys.argv[1]:
                fetch.restart()
            else:
                print("Unknown command")
                sys.exit(2)
            sys.exit(0)
        else:
            print("Usage: %s start|stop|restart" % sys.argv[0])
            sys.exit(2)
    except Exception as e:
            print("Exception: " + e)
            print('-'*60)
            traceback.print_exc(file=sys.stdout)
            print('-'*60)
