import os,os.path
from os.path import normpath,join
from os import chdir,remove
def VisitDir(arg,dirname,names):
    for filepath in names:
        if filepath[-1:] == '~':
            print normpath(join(dirname,filepath))
            remove(normpath(join(dirname,filepath)))
if __name__ == "__main__":
    path = "d:\\"
    os.path.walk(path,VisitDir,0)
