
import os, socket, platform, asyncio, shlex
from requests import get
from colorama import *

os.system('cls')
os.system('title JTERM@'+platform.node())
init(convert=True)


""" ERROR CLASSES (IGNORE) """


class Err:
    def __init__(self, error_name, details):
            self.error_name = error_name
            self.details = details
        
    def __repr__(self):
        result  = f'{self.error_name}: \'{self.details}\'\n'
        return result

class InvalidSyntax(Err):
    def __init__(self, details):
        super().__init__('InvalidSyntaxErr', details)

class FileNotFound(Err):
    def __init__(self, details):
        super().__init__('FileNotFoundErr', details)

class RequiredParam(Err):
    def __init__(self, details):
        super().__init__('RequiredParamErr', details)

class ConnectionDenied(Err):
    def __init__(self, details):
        super().__init__('ConnectionDeniedErr', details)

class AccessDenied(Err):
    def __init__(self, details):
        super().__init__('AccessDeniedErr', details)


class JTERM:

    def __init__(self):  

        self.main_input = input(rf'({os.getcwd()}){Fore.LIGHTGREEN_EX} {platform.node()}{Fore.YELLOW} @ {platform.platform()}' + '\n' + fr'{Fore.RESET} @ ')
        self.shlex_split = shlex.split(self.main_input)
        self.INFO = {

        
            'platform': platform.system(),
            'platform-version': platform.version(),
            'hostname': socket.gethostname(), 
            'ip-address': socket.gethostbyname(socket.gethostname()),
            'public-ip': self.public_ipv4(),
            'processor': platform.processor(),
            'release': platform.release(),
            'cwd': os.getcwd(),
            

        }
        
        
        try:
            if 'cd' in self.shlex_split[0]:
                try:
                    os.chdir(self.main_input[3:])
                except Exception:
                    print(FileNotFound(f'{self.main_input[3:]}'))


            elif 'ld' in self.shlex_split[0]:
                self.ld()

            elif 'wf' in self.shlex_split[0]:
                self.wf()

            elif 'puts' in self.shlex_split[0]:
                self.puts()

            elif 'rl' in self.shlex_split[0]:
                self.rl()
            
            elif 'mdir' in self.shlex_split[0]:
                self.mdir()
            
            elif 'rf' in self.shlex_split[0]:
                asyncio.run(self.rf())


            elif self.shlex_split[0] in self.INFO:
                print(self.INFO[self.shlex_split[0]])
            
            else:
                print(InvalidSyntax(str(self.main_input)))

        except Exception:
            pass
        
    

    def rf(self):

        try:
            with open(self.shlex_split[1], 'r') as w:
                print(f'{Fore.LIGHTBLUE_EX}{w.read()}{Fore.RESET}')

                if 'w|o' in self.shlex_split[2]:
                    with open(self.shlex_split[3], 'w') as x:
                        r = w.read()
                        x.write(r)
                return w

        except FileNotFoundError or FileExistsError:
            print(FileNotFound(f'{self.shlex_split[1]}'))


    def wf(self):

        """
        THE FUNCTION OF WF IS TO CREATE A FILE.
        e.g.
        >> wf foo/bar/hello_world.txt
        << File created: 'hello_world.txt'
            """

        try:
            with open(self.shlex_split[1], 'w', encoding='utf-8') as w:
                w.write(self.shlex_split[2:])
                w.close()

        except Exception:
            AccessDenied(f'{self.shlex_split[1]} cannot be created.')
    
    def rl(self):
        try:

            total_lines = 0
            total_char = 0

            with open(self.main_input[3:], 'r', encoding='utf-8') as f:
                

                for line in f.readlines():
                    total_lines += 1

                f.read()
                return f.read(), print(f'{Fore.LIGHTBLUE_EX} counted a total of {total_lines} lines. {Fore.RESET}')

        except Exception:
            FileNotFound(self.main_input[3:])
    
    def puts(self):

        """
        PUTS IS USED FOR PRINTING STRING TO THE CONSOLE.
        THIS COMMAND CLOSELY RESEMBLES 'echo' FROM THE WINDOWS SHELL (WITHOUT % FUNCTION).
        e.g. 
        >> puts hello world!
        << hello world!
        """
        
        try:
            if 'w|o' in self.shlex_split:
                index = self.shlex_split.index('w|o') + 1
                with open(self.shlex_split[3], 'w') as x:
                    x.write(self.main_input[5:].split(index[-1]))
            else:
                print(self.main_input[5:])

        except Exception:
            InvalidSyntax(self.main_input[5:])
        
        return


    def ld(self):

        """
        LD IS USED FOR LISTING A SPECIFIED/CURRENT DIRECTORY.
        LD ALSO RETURNS THE AMOUNT OF CHARACTERS SPECIFIED IN THE FILE AND THE AMOUNT OF LINES COUNTED IN THE FILE.
        e.g.
        >> ld root/foo/bar/
        << main.py \n helloworld.txt \n password_secret.txt \n etc.etc
        """

        try:

            total_files = 0

            for f in os.listdir(os.getcwd()):
                total_files += 1
                print(f'{Fore.LIGHTBLUE_EX}> {f} {Fore.RESET}')

            print(f'{Fore.LIGHTBLUE_EX} counted a total of {total_files} file(s). {Fore.RESET}')

            return f

        except Exception: 
            return FileNotFound(self.main_input[3:])
    
    def public_ipv4(self):

        """
        PUBLIC-IPV4 IS USED FOR RETURNING THE SPECIFIED COMPUTERS PUBLIC IPV4 ADDRESS VIA 'https://api.ipify.org'
        e.g.
        >> 'public-ip'
        << 12.34.5678
        """
        try:

            ip = get('https://api.ipify.org/').text
            return ip

        except Exception:
            ConnectionDenied('Connection unable to be preformed.')


    def getscrape(self):
        try:
            result = get(self.shlex_split[1]).text
            with open(rf'{self.shlex_split[2]}', 'w') as f:
                f.write(result)
                print(f'Saved to {self.shlex_split[2]}')
                f.close()
            return result

        except Exception:
            pass

    def mdir(self):

        """
        MDIR HAS THE SAME FUNCTION AS 'os.mkdir()'
        e.g.
        >> mdir foo/bar/buzz.txt
        << Directory created: 'buzz.txt'
        """

        try:
            os.mkdir(self.shlex_split[1:])
            print(rf'Directory created @ \'{self.shlex_split[2:]}\'')
        except Exception:
            AccessDenied(f'File {self.shlex_split[2:]} is not permitted to be overwritten/created in this specific directory.')

if __name__ == '__main__':
    while True:
        JTERM()
