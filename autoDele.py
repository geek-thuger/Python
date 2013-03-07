from os.path import walk,join,normpath
from os import chdir,remove
import os
def scan(arg,dirname,names):
    for file in names:
        if file[-1:] == '~':
            files = normpath(join(dirname,file))
            chdir(dirname)
            print "deleting",files
            remove(file)
            print "done!"
if __name__=="__main__":
    path = "d:\\"
    os.path.walk(path,scan,0)
