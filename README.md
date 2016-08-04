# WindowsServer DNSLog Cleaner
Daemon scipt that clean windows server DNS log file and insert them into a database for analysis.
The database can be any SQL-based database of your choice, We are picking MYSQL for the current time.



### Useful comands for cronTabs in UNIX systems
> crontab -e      

> crontab -l

> crontab -r

> crontab -v


### Running script with crontab
> @reboot * 12 * * * sudo python /home/to/the/main.py start &

### How to run/stop/restat without crontab
> python main.py start

> python main.py stop

> python main.py restart

### view the crontab script
> ps aux | grep /home/to/the/script.py


### Upgrade setup tools
> pip install --upgrade setuptools

> easy_install -U setuptools

> pip install setuptools --no-use-wheel --upgrade

### Install prerequisties
> sudo apt-get install python-dev libmysqlclient-dev  # Debian / Ubuntue
> Sudo yum install python-dev mysql-devel



### How to view the daemon
>  ps ax

### Daemon Used
> https://github.com/serverdensity/python-daemon
