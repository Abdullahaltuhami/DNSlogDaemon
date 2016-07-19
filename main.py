#!/usr/bin/env python3
import sys,time,io
from daemon import Daemon


s = 'Strating script..'
d = 'daemon Initiated'
print(s +'\n'+ d)

class DnslogDaemon(Daemon):
    def run(self):
        with io.FileIO("Daemon-test.txt","w") as file:
            file.write("Daemon is succuessfully running")

if __name__ == '__main__':
    daemon = DnslogDaemon('/tmp/dnsDaemon-example.pid')
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
        sys.ecit(0)
    else:
        print("Usage: %s start|stop|restart " % sys.argv[0])
        sys.exit(2)
