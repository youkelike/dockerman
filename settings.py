
DATABASES = dict(
    DB='docker',
    USER='root',
    PASSWD='111',
    HOST='localhost',
    PORT=3306
)

TEMPLATE_VARIABLES = dict(
    title=u'Docker管理平台',
    name=u'Docker管理平台' ,
    username='',
)

NODE_LIST = ['node_ip','port']

COOKIE_NAME = 'user_id'