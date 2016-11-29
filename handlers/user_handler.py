from .base import BaseHandler
from models.check import Check
from settings import COOKIE_NAME

class Login(BaseHandler):
    def get(self):
        self.render('user/login.html',
                    login_strings=dict(username='Usernae',password='Password'))

    def post(self, *args, **kwargs):
        input_username = self.get_argument('username')
        input_password = self.get_argument('password')
        #验证用户时需要与数据库交互，放到单独的模块中
        check_result = Check.login_check(input_username,input_password)
        if check_result == 'Invalid user':
            self.render('user/login.html',
                        login_strings=dict(username='Invalid Usernae',password='Password'))
        elif check_result == 'Incorrect password':
            self.render('user/login.html',
                        login_strings=dict(username='Usernae', password='Incorrect Password'))
        elif check_result == 'admin':
            #登录成功才注入cookie,cookie键名可配置，值是用户名
            self.set_secure_cookie(COOKIE_NAME,input_username,expires_days=1)
            self.redirect('/main')
        else:
            self.set_secure_cookie(COOKIE_NAME,input_username,expires_days=1)
            self.redirect('user/login.html')

class Logout(BaseHandler):
    def get(self):
        #登出操作就是清除当前用户cookie
        self.clear_cookie(COOKIE_NAME)
        self.write('<script>top.window.location.href="/";</script>')


