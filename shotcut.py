import os, winshell, win32com.client
import pythoncom

desktop = winshell.desktop()
#desktop = r"path to where you wanna put your .lnk file"

path = os.path.join(desktop, 'File Shortcut Demo.lnk')
target = r"G:\PROGRAMMING\ALPHA PROJECTS\autoshudown\shotcut.py" 
icon = r"lf2.ico"

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()