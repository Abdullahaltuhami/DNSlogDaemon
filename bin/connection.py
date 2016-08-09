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


class fetcher(Daemon):
    def run(self):
        cp_from = '/home/rwx/Desktop/winshare/Users/abdullah.altuhami/Documents'
        cp_to = '/home/rwx/Desktop'
        for path_from in glob.glob(cp_from+'/DNS*'):
            cmd = '{0} {1} {2}'.format('cp',path_from,cp_to)
        os.system(cmd)

if __name__ == '__main__':
    try:
        con = connect()

        fetch = fetcher('/tmp/OGC-fetcher-daemon.pid')
        fetch.start()
        #con.set_connection()
    except Exception as e:
        print(e)
