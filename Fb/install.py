#!usr/bin/python3
import sys
import platform
import os


def LibPath():
    global LibPath
    try:
        LibPath = sys.path[4]
        print('[*]Found Python Library Path!')
        print('>>>',str(LibPath))
    except:
        print('[!]Failed to install Fb.py.\n[!]Try Method 2.\n>> https://github.com/DeadOnTheInsideCoder/Fb/blob/master/README.md.')
        sys.exit()


def FbPath():
    global FbPath
    FbPath = sys.path[0]+'\Fb.py'

def FindOs():
    global Os
    Os = platform.system()
    print('[*]Found Os! \n>>',str(Os))

def Move():
    global LibPath
    global FbPath
    global Os
    if Os == 'Windows':
        command = 'move '+'"'+FbPath+'"'+' '+'"'+LibPath+'"'
        os.popen(command)
    elif Os == 'Linux':
        command = 'mv'+'"'+FbPath+'"'+' '+'"'+LibPath+'"'
        os.popen(command)
    elif Os == 'Darwin':
        command = 'mv'+'"'+FbPath+'"'+' '+'"'+LibPath+'"'
        os.popen(command)
    else:
        print('[!]Failed to install Fb.py.\n[!]Try Method 2.\n>> https://github.com/DeadOnTheInsideCoder/Fb/blob/master/README.md.')
        sys.exit()

def Check():
    try:
        import Fb
        print('[*]Fb Succesfully installed.')
        sys.exit()
    except Exception as e:
        print(str(e))
        print('[!]Failed to install Fb.py.\n[!]Try Method 2.\n>> https://github.com/DeadOnTheInsideCoder/Fb/blob/master/README.md.')
        sys.exit()
def Install():
    
    print('[!]Installing...')
    LibPath()
    FbPath()
    FindOs()
    Move()
    Check()
    
Install()
