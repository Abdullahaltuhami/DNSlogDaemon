# DNSlogDaemon
Daemon scipt that clean windows server DNS log file and insert them into a database for analysis.
The database can be any SQL-based database of your choice, We are picking MYSQL for the current time.



### Useful comands for cronTabs in UNIX systems 
> crontab -e      

> crontab -l

> crontab -r

> crontab -v


### Running script with crontab
> @reboot * 12 * * * sudo python /home/to/the/script.py &

### view the crontab script 
> ps aux | grep /home/to/the/script.py

### How to run/stop/restat the daemon
> python main.py start

> python main.py stop

> python main.py restart


### How to view the daemon
>  ps ax
