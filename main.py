
from os.path import join,exists
from os import scandir


def main(were='.'):
    Cclass = [were] ; CP = were ; loop = 0 , files , dirs = []
    print(f'trying to find the '+fg('cyan')+ 'ProxyServer'+fg('white'))
    while len(Cclass) != 0:
        try:
            for i in scandir(CP):
                if i.is_dir():
                    Cclass.append((var:=join(CP,i.name))) ; dirs.append((var:=join(CP,i.name)))
                else:
                    files..append((var:=join(CP,i.name)))
            Cclass.remove(CP)
            return CP , files , dirs
            CP = Cclass[0]
        except Exception as er: 
            pass

main('/sdcard')
