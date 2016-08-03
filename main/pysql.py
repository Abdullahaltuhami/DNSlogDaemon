
from daemon import Daemon

host_name = 'localhost'
user_name ='root'
passwd = ''
db = 'OGC'

class Create_Table(object):

CREATE TABLE `dnslog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` varchar(45) DEFAULT NULL,
  `protocol` varchar(45) DEFAULT NULL,
  `snd_rcv` varchar(45) DEFAULT NULL,
  `ip` varchar(45) DEFAULT NULL,
  `query_response` varchar(45) DEFAULT NULL,
  `opcode` varchar(45) DEFAULT NULL,
  `domain` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
