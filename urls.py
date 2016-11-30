from handlers.user_handler import Login,Logout
from handlers.node_handler import  Main,\
                                    NodeManage,\
                                    Top,\
                                    LeftGroup,\
                                    GroupList,\
                                    RightNode,\
                                    ConCreate,\
                                    ConAction,\
                                    ConStart,\
                                    ConStop,\
                                    ConDestroy,\
                                    ConRestart,\
                                    ConManage,\
                                    ConModify

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
    (r'/concreate',ConCreate),
    (r'/conaction',ConAction),
    (r'/constart',ConStart),
    (r'/constop',ConStop),
    (r'/conrestart',ConRestart),
    (r'/condestroy',ConDestroy),
    (r'/conmanage',ConManage),
    (r'/conmodify',ConModify),
]