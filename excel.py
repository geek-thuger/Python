from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app:showwarning(app,'Exit?')
RANGE = rane(3,8)

def excel():
    app = 'Excel'
    xl  = win32.gencache.EnsureDispatch('%s.Application'%app)
    ss= xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.VIsible = True
    sleep(1)

    sh.Cells(1,1).Value = 'Python-to-%s Demo'%app
    sleep(1)
    sh.Cells(i+2,1).Value = "Th-th-th-that's all folks!"

    warn(app)
    ss.Close(False)
    xl.Application.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    excel()
