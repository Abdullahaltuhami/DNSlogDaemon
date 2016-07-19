# DNSlogDaemon
The DNSlogDaemon is a script runs in the background as a daemon process. The script main job is to clean the DNS log of a server and feed it
to a database for analaysis.
The database can be anyy SQL-based database of your choice, We are picking postgresDB.

### Prerequisite
* Python 2
* python-daemon by sander Marechal
* postgressDB

### How to run/stop/restat the daemon
##### Starting Daemon
- python main.py start
##### Stoping Daemon
- python main.py stop
##### Restarting Daemon
- python main.py restart

### How to view the daemon
View all by
>  ps ax
