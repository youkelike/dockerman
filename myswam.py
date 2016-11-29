import docker
import socket
from curl import Curl

class Myswam(object):
    def ping_port(self,ip,port):
        '''尝试跟管理端口建立连接，而不仅是ping'''
        cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        cs.settimeout(0.2)
        address = (str(ip),int(port))
        try:
            cs.connect((address))
        except socket.error as e:
            print(e)
            return 1
        cs.close()
        return 0

    def _container_detail(self,node_ip,node_port,container_id):
        url = 'http://%s:%s/containers/%s/json' % (node_ip,node_port,container_id)
        container_more_curl = Curl(url)
        ret_json = container_more_curl.get_value()
        return ret_json

    def container_list(self,node_ip,node_port):
        url = 'http://%s:%s/containers/json?all=1' % (node_ip,node_port)
        container_curl = Curl(url)
        ret_json = container_curl.get_value()

        con_data = {}
        container_id = []
        if ret_json:
            for i in ret_json:
                container_id.append(i['Id'][0:12])
        else:
            return con_data

        if len(container_id) < 1:
            return con_data
        else:
            con_data = {}
            con_num = 1
            for con_id in container_id:
                tmp_dict = {}
                ret_json = self._container_detail(node_ip, node_port, con_id)
                if len(ret_json) < 1:
                    return con_data
                con_state = ""
                if ('Running' in ret_json['State'].keys()) and (
                            'Status' not in ret_json['State'].keys()):  # for docker 1.7
                    con_state = str(ret_json['State']['Running'])
                elif 'Status' in ret_json['State'].keys():  # for docker 1.9 and higher
                    con_state = str(ret_json['State']['Status'])
                else:  # for else
                    con_state = "Exited"
                tmp_dict['id_num'] = ret_json['Id'][0:12]
                tmp_dict['con_ip'] = ret_json['NetworkSettings']['IPAddress']
                tmp_dict['name'] = ret_json['Name']
                tmp_dict['cpuperiod'] = ret_json['HostConfig']['CpuPeriod']
                tmp_dict['cpuquota'] = ret_json['HostConfig']['CpuQuota']
                tmp_dict['memory'] = ret_json['HostConfig']['Memory']
                tmp_dict['state'] = con_state
                tmp_dict['cmd'] = str(ret_json['Config']['Cmd'])
                tmp_dict['created'] = ret_json['State']['StartedAt']
                con_data[con_num] = tmp_dict
                con_num += 1
        return con_data
