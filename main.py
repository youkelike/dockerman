import os,sys

import tornado.httpserver
import tornado.web
import tornado.ioloop
from tornado.options import define,options,parse_command_line

from urls import urls

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
define('port',default=8000,type=int,help='run on the port')

if __name__ == '__main__':
    SETTINGS = dict(
        template_path=os.path.join(os.path.dirname(__file__),'templates'),
        static_path=os.path.join(os.path.dirname(__file__),'statics'),
        login_url='/login',
        cookie_secret='lsdgjo480239osidfalsdjgg948023wo234398hgb'
    )
    parse_command_line()
    print('sever listen port %s' % options.port)
    application = tornado.web.Application(
        handlers=urls,
        **SETTINGS
    )
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()