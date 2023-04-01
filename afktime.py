from win32api import GetTickCount,GetLastInputInfo
from tkinter import Tk,Label
from time import sleep
from os import system
from PIL import Image
from pystray import Icon as Ic,Menu as Mn,MenuItem as MnI

def getIdleTime():
    return (GetTickCount() - GetLastInputInfo()) / 1000.0

def shutdown():
    # print("System Shutdown")
    system("shutdown /s /t")

strayicon=Image.open("stray.png")

class Adminpanel:
    def __init__(self) -> None:
        self.adminwin=Tk()
        self.icon=Ic("AKF",strayicon,"AFK Moniter",
                menu=Mn(
                    MnI("Admin Panel",self.showadminpanel())
                )
            )
        self.adminwin.title("AFK Moniter Admin Panel")
        self.adminwin.geometry("500x500")
        self.adminwin.withdraw()
        self.icon.run()
        self.afkcheck()
        self.adminwin.mainloop()

    def warningwindow(self):
        self.warwin=Toplevel(self.adminwin)
        self.i=30
        self.warwin.title("WARING WINDOW")
        self.warwin.geometry("400x300")
        self.warwin.columnconfigure(0, weight=0)
        self.warwin.rowconfigure(0, weight=0)
        
        self.message=Label(self.warwin,text="System is going to Shutdown in ...",font=("arial",17))
        self.message.pack()
        self.label=Label(self.warwin,text="00",font=("arial",200))
        self.label.pack()
        self.warwin.protocol("WM_DELETE_WINDOW", self.stopshutdown)
        self.start()
        self.warwin.mainloop()


    def showadminpanel(self):
        self.adminwin.deiconify()

    def start(self):
        self.label.config(text=f"{self.i}")
        if self.i==0:
            shutdown()
        else:
            self.label.after(1000,self.start)
            self.i-=1
    
    def stopshutdown(self):
        print("Shutdown Process Terminated")
        self.warwin.destroy()
        self.afkcheck()

    def afkcheck(self):
        while True:
            print("check")
            if getIdleTime()>=5:
                print("starting countdown")
                self.warningwindow()
                

ap=Adminpanel()