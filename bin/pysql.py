import MySQLdb
import traceback




class PySql(object):
    host_name = 'localhost'
    user_name = 'root'
    passwd = 'rootserver'
    db_schema = 'OGC'

    def create_table(self):
        try:
            db = MySQLdb.connect(
                host=self.host_name,user=self.user_name, passwd=self.passwd, db=self.db_schema)
            cursor = db.cursor()
            cursor.execute('''
            CREATE TABLE `dnslog` (
                                  `id` int(11) NOT NULL AUTO_INCREMENT,
                                  `date_time` varchar(45) DEFAULT NULL,
                                  `context` varchar(45) DEFAULT NULL,
                                  `protocol` varchar(45) DEFAULT NULL,
                                  `direction` varchar(45) DEFAULT NULL,
                                  `ip` varchar(45) DEFAULT NULL,
                                  `r_q` varchar(45) DEFAULT NULL,
                                  `opcode` varchar(45) DEFAULT NULL,
                                  `response_code` varchar(45) DEFAULT NULL,
                                  `domain` varchar(500) DEFAULT NULL,
                                  `exception` varchar(1500) DEFAULT NULL,
                                  PRIMARY KEY (`id`),
                                  UNIQUE KEY `id_UNIQUE` (`id`)
                                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

                           ''')
            db.commit()
        except Exception as e:
            print(e)

    def check_table(self):
        try:
            db = MySQLdb.connect(
                host=self.host_name,user=self.user_name, passwd=self.passwd, db=self.db_schema)
            cursor = db.cursor()

            cursor.execute('''
                           SELECT COUNT(*)
                           FROM information_schema.TABLES
                           WHERE table_name = 'dnslog'
                           ''')
            if cursor.fetchone()[0] == 1:
                return True

            return False
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def priv(self):
        try:
            db = MySQLdb.connect(
                host=self.host_name,  user=self.user_name, passwd=self.passwd, db=self.db_schema)
            cursor = db.cursor('''GRANT ALL privileges ON *.* TO 'root'@'localhost' identified by 'root' with grant option''')
        except Exception as e:
            print(e)
