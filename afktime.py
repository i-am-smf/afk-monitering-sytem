from win32api import GetTickCount,GetLastInputInfo
from tkinter import Tk,Label
from time import sleep
from os import system

def getIdleTime():
    return (GetTickCount() - GetLastInputInfo()) / 1000.0

def shutdown():
    # print("System Shutdown")
    system("shutdown /s /t")

class Countdown:
    def __init__(self) -> None:
        self.i=30
        self.startcounting()
    def startcounting(self):
        self.warwin=Tk()

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


while True:
    sleep(100)
    if getIdleTime()>=600:
        # print("starting countdown")
        Countdown()