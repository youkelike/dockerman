import tornado.web
from settings import COOKIE_NAME,TEMPLATE_VARIABLES
from models.user import UserSqlOperation

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        TEMPLATE_VARIABLES['username'] = self.get_secure_cookie(COOKIE_NAME)
        return self.get_secure_cookie(COOKIE_NAME)

    def check_authenticated(self):
        '''简单的权限验证，只验证user表的user_group字段'''
        user_name = self.get_secure_cookie(COOKIE_NAME)
        mysql_adm_password = UserSqlOperation.check_adm_login(user_name)
        user_group = mysql_adm_password[0][2]
        if user_group != 'admin':
            self.redirect('/')