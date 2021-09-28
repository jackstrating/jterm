
"""CREDIT JACK STRATING IF YOU ARE USING THIS IN COMMERCIAL PRODUCTS."""
"""ALL RIGHTS RESERVED, JACK STRATING, 2021"""


import os
import platform
import sys
import socket
from colorama import*
from requests import get
import base64
from tkinter import*
import ctypes


init(convert=True)
os.system('cls' or 'clear')

print(f"""
{Style.DIM}JTERM v.1.1.1
by Jack Strating, all rights reserved.
https://www.github.com/jackstrating/jterm
""")


RUN = True
ROOT = False



def out(r, t) -> str:
    print(f'{Fore.LIGHTGREEN_EX}stdout {Fore.LIGHTMAGENTA_EX}<< {Fore.WHITE}{t}\n') 

class settings:

    def __init__(self):
        pass


class argvar(settings):

    def argvar() -> list:
        try:
            out(0, sys.argv)
        except Exception as e:
            out(1, e)


class puts(settings):

    def puts(t) -> str:
        try:
            out(0, t)
        except Exception as e:
            out(1, e)


class rf(settings):

    def rf(f) -> str:
        try:
            with open(f, 'r', encoding='utf-8') as a:
                out(0, a.read())
        except Exception as e:
            out(1, e)


class ld(settings):

    def ld() -> str:
        try:
            total = 0
            for f in os.listdir():
                total += 1
                print(f'{Fore.LIGHTBLUE_EX}> {f}')
            out(0, f'counted {Fore.CYAN}{total}{Fore.RESET} files.')
        except Exception as e:
            out(1, e)


class kill(settings):

    def kill(t) -> str:
        try:
            out(0, os.system(f'taskkill /F /IM {t}'))
        except Exception as e:
            out(1, e)


class uname(settings):

    def uname() -> str:
        try:
            out(0, platform.node())
        except Exception as e:
            out(1, e)


class node(settings):

    def node() -> str:
        try:
            out(0, platform.node())
        except Exception as e:
            out(1, e)


class getmac(settings):

    def getmac():
        try:
            os.system('getmac')
        except Exception as e:
            out(1, e)


class cl(settings):

    def cl() -> 0:
        try:
            out(0, os.system('cls'))
        except Exception as e:
            out(1, e)


class cwd(settings):

    def cwd() -> str:
        try:
            out(0, os.getcwd())
        except Exception as e:
            out(1, e)


class py(settings):

    def py(t) -> str:
        try:
            out(0, exec(t))
        except Exception as e:
            out(1, e)


class ipinternal(settings):

    def ipinternal() -> str:
        try:
            out(0, get('https://api.ipify.org').text)
        except Exception as e:
            out(1, e)


class cd(settings):

    def cd(direc) -> 0:
        try:
            out(0, os.chdir(direc))
        except Exception as e:
            out(0, e)
        

class db64f(settings):

    def db64(f) -> str:
        try:
            decoded = open(f,'r')
            out(0, base64.b64decode(str(decoded.read())))
        except Exception as e:
            out(1, e)


class eb64f(settings):

    def eb64(f) -> str:
        try:
            encoded = open(f,'r')
            out(0, base64.b64encode(str(encoded.read())))
        except Exception as e:
            out(1, e)

class eb64(settings):
    def eb64(t) -> str:
        try:
            t.encode('ascii')
            encoded = base64.b64encode(bytes(t, encoding='utf-8'))
            out(0, encoded)
        except Exception as e:
            out(1, e)


class db64(settings):
    def db64(t) -> str:
        try:
            decoded = base64.b64decode(t)
            out(0, decoded)
        except Exception as e:
            out(1, e)


class run:

    def run(f) -> 0:
        try:
            os.system(f'start {f}')
        except Exception as e:
            out(1, e) 


class backg:

    def backg(f) -> 0:
        try:
            if out(0, ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{f}' , 0)) == False:
                pass
            else:
                out(0, ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{f}' , 0))
        except Exception as e:
            out(1, e)


def main():

    mi = input('(' + str(os.getcwd()) + ') ' + Fore.LIGHTGREEN_EX + 
    str(os.getlogin()) + "@" + str(platform.node()) + 
    Fore.LIGHTMAGENTA_EX + " " + str(platform.system()) + 
    Fore.YELLOW + " ~" + "\n" +
    Fore.WHITE + '& ')

    if 'puts' in mi[0:4]:     
        out(0, str(mi[4:]))

    elif 'rf' in mi[0:2]:
        rf.rf(mi[3:])

    elif 'ld' in mi[0:2]:
        ld.ld()

    elif 'kill' in mi[0:4]:
        kill.kill(mi[5:])

    elif 'uname' in mi[0:5]:
        uname.uname()

    elif 'getmacaddr' in mi[0:10]:
        getmac.getmac()

    elif 'cl' in mi:
        cl.cl()

    elif 'node' in mi[0:4]:
        node.node()

    elif 'cwd' in mi[0:3]:
        cwd.cwd()
        
    elif 'py' in mi[0:2]:
        if '--s' or '-s' in mi:
            while True:
                loop = py.py(input(f'{Fore.LIGHTGREEN_EX}py {Fore.LIGHTMAGENTA_EX}>>> {Fore.RESET}'))
                return loop

        else:
            py.py(mi[4:])
    
    elif 'db64f' in mi[0:5]:
            db64f.db64(mi[6:])
    
    elif 'eb6f' in mi[0:5]:
        eb64f.eb64(mi[6:])

    elif 'eb64' in mi[0:4]:
        eb64.eb64(mi[0:5])
    
    elif 'db64' in mi[0:4]:
        db64.db64(mi[0:5])

    elif 'ip' in mi[0:2]:
        ipinternal.ipinternal()
    
    elif 'argvar' in mi[0:6]:
        argvar.argvar()

    elif 'cd' in mi[0:2]:
        cd.cd(mi[3:])

    elif 'exit' in mi[0:4]:
        sys.exit()

    elif 'run' in mi[0:3]:
        if '.py' in mi:
            os.system(f'python {mi[4:]}')
        run.run(mi[4:])
    
    elif 'backg' in mi[0:5]:
        backg.backg(mi[5:])



    else:
        out(1, f'"{mi}" is not a recognized command. type "help" for more information.')


if __name__ == '__main__':
    while True:
        if RUN == True:
            main()

