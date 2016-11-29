import os,json
import pycurl
from io import BytesIO

class Curl(object):
    def __init__(self,curl):
        self.__curl__ = curl

    def get_value(self):
        d_url = pycurl.Curl()
        url_buf = BytesIO()
        d_url.setopt(d_url.URL,self.__curl__)
        try:
            d_url.setopt(d_url.WRITEFUNCTION,url_buf.write)
            d_url.perform()
        except pycurl.error as e:
            errno,errstr = e
            print('An error occured:',errstr)
        #需要事先约定返回数据格式是json
        ret_json = json.loads(url_buf.getvalue().decode())
        return ret_json

    def post_value(self,action,param):
        pass