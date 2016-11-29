from .mysql_server import MysqlServer
from settings import DATABASES

class UserSqlOperation(object):
    @staticmethod
    def check_adm_login(admname):
        db = MysqlServer(DATABASES)
        sql = 'select name,password,user_group from user where name="%s"' % admname
        ret = db.sql_query(sql)
        db.close()
        return ret