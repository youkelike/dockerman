from sqlalchemy import create_engine,text,update
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:111@localhost:3306/docker?charset=utf8',
                       echo=True,#会打印创建数据库过程
                       encoding='utf-8',
                       pool_size=1000,
                       pool_recycle=3600,
                       )
Base = declarative_base()

class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    node_ip = Column(String(32))
    port = Column(String(32))
    cpus = Column(String(32))
    mem = Column(String(32))
    images = Column(String(32))
    state = Column(String(32))
    node_group = Column(String(32))
    containers = Column(String(32))
    os_version = Column(String(32))
    kernel_version = Column(String(32))
    docker_version = Column(String(32))

    def __repr__(self):
        return '<Node(name=%s,ip=%s,port=%s,cpus=%s,mem=%s,images=%s,' \
               'state=%s,node_group=%s,containers=%s,os_version=%s,kernel_version=%s,' \
               'docker_version=%s)>' % (
                self.name,self.node_ip,self.port,self.cpus,self.mem,self.images,
                self.state,self.node_group,self.containers,self.os_version,self.kernel_version,
                self.docker_version
                )

class ConUsage(Base):
    __tablename__ = 'con_usage'
    id = Column(Integer,primary_key=True)
    con_id = Column(String(64))
    con_ip = Column(String(32))
    node_ip = Column(String(32))
    user_name = Column(String(32))
    con_app = Column(String(32))
    con_desc = Column(String(32))

    def __repr__(self):
        return '<Consumer(con_id=%s,con_ip=%s,node_ip=%s,' \
               'user_name=%s,con_app=%s,con_desc=%s)>' % (
                self.con_id,self.con_ip,self.node_ip,
                self.user_name,self.con_app,self.con_desc
                )

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    user_group = Column(String(32))

    def __repr__(self):
        return '<User(name=%s,password=%s,user_group=%s)>' % (
                    self.name,self.password,self.user_group
                )

if __name__ == '__main__':
    Base.metadata.create_all(engine)