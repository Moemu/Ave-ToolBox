'''
此类用于存放各工具源码
'''
import subprocess
from OtherTool import *

def WallPaperLock(Status:int):
    '''
    锁定壁纸
    '''
    CreatKey(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Policies','ActiveDesktop')
    WriteValue(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop','NochangingWallpaper',win32con.REG_DWORD,Status)
    return None

def WebBrowserLock(Status:int):
    '''
    禁用Microsoft Edge上网
    '''
    if Status == 1:
        subprocess.getstatusoutput('netsh advfirewall firewall add rule name="WebBrowserLock1" dir=out program="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" action=block')
    else:
        subprocess.getstatusoutput('Netsh advfirewall firewall set rule name="WebBrowserLock1" new enable=no')

def SystemToolLock(Status:int):
    '''
    系统工具锁
    '''
    WriteValue(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system','DisableTaskmgr',win32con.REG_DWORD,Status)
    WriteValue(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system','DisableRegistryTools',win32con.REG_DWORD,Status)
    WriteValue(win32con.HKEY_CURRENT_USER,'SOFTWARE\Policies\Microsoft\Windows\System','DisableCMD',win32con.REG_DWORD,Status)
    WriteValue(win32con.HKEY_CURRENT_USER,'SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\EXPLORER','RESTRICTRUN',win32con.REG_DWORD,Status)