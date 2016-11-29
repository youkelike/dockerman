from .base import BaseHandler
import tornado.web
import threading,json

from models.node import NodeInfo
from models.data_manage import DataManage
from myswam import Myswam

from settings import TEMPLATE_VARIABLES

class Main(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('node/main.html')

class NodeManage(BaseHandler):
    @tornado.web.authenticated
    def get(self,*args,**kwargs):
        threads = []
        #异步方式启动一个线程去刷新节点数据，把刷新和获取动作分开
        node_update = threading.Thread(target=self._update_node)
        threads.append(node_update)
        #多启动一个空线程，组成至少两个线程构成线程队列，通过下面的循环来引发内部竞争
        # ，否则会阻塞获取数据的动作
        node_pass = threading.Thread(target=self._get_pass)
        threads.append(node_pass)
        for t in threads:
            t.setDaemon(True)
            t.start()
        node_data = NodeInfo.node_info()
        node_data_handled = DataManage.manage_node_info(node_data)
        self.render('node/node_manage.html',
                    node_data=node_data_handled)

    def _update_node(self):
        node_data = NodeInfo.node_info()
        myswarm = Myswam()
        for line in node_data:
            node_ip = line[2]
            node_port = line[3]
            #用ping测试容器是否运行中,否则在更新数据时会被阻塞一个较长的默认的连接等待时间
            #还能用与报告容器状态
            if myswarm.ping_port(node_ip,node_port) == 1:
                continue
            else:
                node_info = myswarm.node_list(node_ip,node_port)
                NodeInfo.node_info_update(node_info,node_ip)

    def _get_pass(self):
        pass

class Top(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('base.html',name=TEMPLATE_VARIABLES)

class LeftGroup(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('node/leftgroup.html')

class GroupList(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        id = self.get_argument('id',None)
        lv = self.get_argument('lv',None)
        name = self.get_argument('n',None)
        alldata = []
        if id == None and lv == None and name == None:
            alldata = self._getGroup()
        elif id != '' and lv == '0':
            alldata = self._getNode(id,name)
        elif lv == '1':
            alldata = self._getContainer(id,name)
        self.write(json.dumps(alldata))

    def _getGroup(self):
        group_data = []
        group_ret = NodeInfo.group_list()
        for i in DataManage.group_list(group_ret):
            group_data.append(i)
        return group_data

    def _getNode(self,id,name):
        node_ret = NodeInfo.node_list(name)
        node_data = DataManage.node_list(node_ret,id,name)
        return node_data

    def _getContainer(self,id,name):
        container_ret = NodeInfo.container_list(name)
        container_data = DataManage.container_list(container_ret,id,data)
        return container_data

class RightNode(BaseHandler):
    @tornado.web.authenticated
    def get(self,*args,**kwargs):
        node_ip = self.get_argument('node_ip',None)
        if node_ip is None:
            self.write('Error')
            return
        else:
            node_port = NodeInfo.get_node_port(node_ip)
            #使用curl去请求docker提供的restful接口，获取节点上的容器列表
            myswam = Myswam()
            con_data = myswam.container_list(node_ip,node_port[0][0])
            self.render('node/rightnode.html',con_data=con_data,node_ip=node_ip)