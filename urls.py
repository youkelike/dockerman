from handlers.user_handler import Login,Logout
from handlers.node_handler import  Main,\
                                    NodeManage,\
                                    Top,\
                                    LeftGroup,\
                                    GroupList,\
                                    RightNode

urls = [
    (r'/',Login),
    (r'/login',Login),
    (r'/logout',Logout),
    (r'/main',Main),
    (r'/nodemanage',NodeManage),
    (r'/base',Top),
    (r'/leftgroup',LeftGroup),
    (r'/grouplist',GroupList),
    (r'/node',RightNode),
]