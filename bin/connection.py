import os
import sys
import traceback

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

    def getFile(self):
        # TODO
        cp_from = '/home/rwx/Desktop/winshare'
        cp_to = '/home/rwx/Desktop/'

if __name__ == '__main__':
    try:
        con = connect()
        con.set_connection()
    except Exception as e:
        print(e)
