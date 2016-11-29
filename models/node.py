from settings import DATABASES
from .mysql_server import MysqlServer

class NodeInfo(object):
    @staticmethod
    def node_info():
        db = MysqlServer(DATABASES)
        sql = 'select * from node'
        ret = db.sql_query(sql)
        db.close()
        return ret

    @staticmethod
    def group_list():
        db = MysqlServer(DATABASES)
        sql = 'select distinct node_group from node'
        ret = db.sql_query(sql)
        db.close()
        return ret

    @staticmethod
    def node_list(group_name):
        db = MysqlServer(DATABASES)
        sql = 'select node_ip from node where node_group="%s"' % group_name
        ret = db.sql_query(sql)
        db.close()
        return ret

    @staticmethod
    def container_list(name):
        pass

    @staticmethod
    def get_node_port(node_ip):
        db = MysqlServer(DATABASES)
        sql = 'select port from node where node_ip="%s"' % node_ip
        ret = db.sql_query(sql)
        db.close()
        return ret