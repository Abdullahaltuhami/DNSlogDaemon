#!/usr/bin/env python
import os
import sys
import traceback
import glob
from daemon import Daemon
import MySQLdb
import time

class connect(object):

    def set_connection(self):
        try:
            if os.path.exists('/home/rwx/Desktop/winshare'):
                print('Directory Already exists')
                os.system('cd /home/rwx/Desktop/winshare')
            else:
                os.system('sudo mkdir -p /home/rwx/Desktop/winshare')
                os.system(
                    'sudo mount.cifs //192.168.15.158/c$ /home/rwx/Desktop/winshare -o user=abdullah.altuhami,domain=oman-gas,password=@bdull@h_94')
        except Exception as e:
            print(e)

    def create_dirs(self):
        os.system('sudo mkdir -p /home/rwx/Desktop/parsing2DB')


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

            cp_from = '/home/rwx/Desktop/winshare/Users/abdullah.altuhami/Documents'
            cp_to = '/home/rwx/Desktop/parsing2DB/'

            for path_from in glob.glob(cp_from + '/DNS*'):
                self.the_file_path = path_from

            creation_date = time.ctime(os.path.getctime(self.the_file_path))
            # If Table is empty copy anyway

            cursor.execute(''' SELECT COUNT(*) FROM information_schema.TABLES WHERE table_name = 'fetchlog' ''')
            if cursor.fetchone()[0] == 1:
                cursor.execute('''INSERT INTO fetchlog(creation_date)VALUES(%s)''',(creation_date))
                db.commit()
            else:
                print('Creation Time of file : ' + creation_date)
                cursor.execute('''SELECT creation_date FROM OGC.fetchlog order by id DESC limit 1''')
                result = cursor.fetchall()
                print('Result of from database is : + result')

                # Not equal means new File was created by server
                if result != creation_date:
                    # If file is new and bigger than 498 MB
                    if os.path.getsize(self.the_file_path) >= 513802240:
                        # Log This file into database
                        cursor.execute('''INSERT INTO fetchlog(creation_date)VALUES(%s)''',
                                       (creation_date))
                        db.commit()

                        # add creation timestamp to file
                        for path_from in glob.glob(cp_from + '/DNS*'):
                            cmd = '{0} {1} {2}'.format(
                                'cp', path_from, cp_to + '-' + creation_date)

                        # Copy it to parsing2DB
                        os.system(cmd)
                    else:
                        print('Something was passed at file size MB checked')
                        pass
                else:
                    print('Something was passed at creation time check')
                    pass

        except:
            print("Exception:")
            print('-'*60)
            traceback.print_exc(file=sys.stdout)
            print('-'*60)


if __name__ == '__main__':
    try:
        fetch = fetcher('/tmp/OGC-fetcher-daemon.pid')
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
        print(e)
