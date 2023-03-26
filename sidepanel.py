from tkinter import *
from win32api import GetTickCount,GetLastInputInfo

def getIdleTime():
    return (GetTickCount() - GetLastInputInfo()) / 1000.0

ws=Tk()
ws.title("AFK Monitoring Panel")
ws.geometry("600x700")

label=Label(ws,text="AFK Monitor")
label.pack()

label2=Label(ws,text=f"Last Input Time : {getIdleTime()}",font=("arial",40))
label2.pack()

def iptupdate():
    label2.config(text=f"System id IDLE for : {int(getIdleTime())} seconds")
    label2.after(1000,iptupdate)

iptupdate()

ws.mainloop()