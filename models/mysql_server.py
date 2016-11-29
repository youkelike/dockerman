import pymysql
import logging
pymysql.install_as_MySQLdb()#与MySQLdb语法兼容
logger = logging.getLogger(__name__)

class MysqlServer(object):
    '''mysql数据库操作模块'''
    def __init__(self,db_config):
        try:
            self._db_config = db_config
            self._conn = self.__get_conn()
            self._cursor = self._conn.cursor()
            logger.info(u'创建数据库连接')
        except Exception as e:
            self.close()
            logger.exception(u'数据库连接失败！')

    def __get_conn(self):
        db_config = self._db_config
        connection = pymysql.connect(host=db_config['HOST'],
                                     port=db_config['PORT'],
                                     user=db_config['USER'],
                                     passwd=db_config['PASSWD'],
                                     db=db_config['DB'])
        connection.ping(True)
        print('*******',connection)
        return connection

    def ensure_cursor(self):
        if not self._cursor:
            if not self._conn:
                self._conn = self.__get_conn()
            self._cursor = self._conn.cursor()

    def sql_query(self,sql):
        '''执行sql并返回结果'''
        self.ensure_cursor()
        self._cursor.execute(sql)
        self._conn.commit()
        return self._cursor.fetchall()

    def sql_execute(self,sql):
        '''只执行sql不返回结果'''
        self.ensure_cursor()
        self._cursor.execute(sql)
        self._conn.commit()

    def sql_fetchone(self,sql):
        '''只返回一条记录'''
        self.ensure_cursor()
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()
        logger.info(u'关闭数据库连接')
