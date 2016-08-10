#!/usr/bin/env python
import os
import sys
import traceback
import glob
from daemon import Daemon
class connect(object):
    def set_connection(self):
        try:
            if os.path.exists('/home/rwx/Desktop/winshare'):
                print('Directory Already exists')
                os.system('cd /home/rwx/Desktop/winshare')
            else:
                os.system('sudo mkdir -p /home/rwx/Desktop/winshare')
                os.system('sudo mount.cifs //192.168.15.158/c$ /home/rwx/Desktop/winshare -o user=abdullah.altuhami,domain=oman-gas,password=@bdull@h_94')
        except Exception as e:
            print(e)

    def create_dirs(self):
        os.system('sudo mkdir -p /home/rwx/Desktop/parsing2DB/notready2parse')
        os.system('sudo mkdir -p /home/rwx/Desktop/parsing2DB/ready2parse')

class fetcher(Daemon):
    def run(self):
        cp_from = '/home/rwx/Desktop/winshare/Users/abdullah.altuhami/Documents'
        cp_to = '/home/rwx/Desktop/parsing2DB/notready2parse'
        for path_from in glob.glob(cp_from+'/DNS*'):
            cmd = '{0} {1} {2}'.format('cp',path_from,cp_to)
        os.system(cmd)

        # If statment

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
