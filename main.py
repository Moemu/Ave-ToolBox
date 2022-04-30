'''
Audio Visual Education Committee tools(电教委员管理工具)
Made by Moemu
Ver: 1.0
Feture: 壁纸锁定, 禁止上网
'''
import PySimpleGUI as sg
import win32api,win32con,subprocess,os

sg.theme('Reddit')

def CreatKey(Rootdirectory=None,Path=None,Keyname=None):
    '''
    在注册表中新建项
    Rootdirectory: 注册表第一层目录
    Path: 注册表下层路径
    Keyname: 项名
    '''
    key = win32api.RegOpenKey(Rootdirectory,Path,0, win32con.KEY_ALL_ACCESS)
    win32api.RegCreateKey(key,Keyname)
    return None

def WriteValue(Rootdirectory=None,Path=None,Keyname=None,Keytype=None,Keyvalue=None):
    '''
    在注册表中写值
    Rootdirectory: 注册表第一层目录
    Path: 注册表下层路径
    Keyname: 值名
    Keytype: 值类型
    Keyvalue: 值
    '''
    key = win32api.RegOpenKey(Rootdirectory,Path,0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,Keyname,0,Keytype,Keyvalue)
    return None

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

def main():
    layout = [
        [sg.Text('电教管理工具(Ver 1.0 By Moemu)',font=('微软雅黑 15'))],
        [sg.Text('注意: 请以管理员模式打开程序, 不然程序无法使用',text_color='red')],
        [sg.Text('锁定壁纸'),sg.Push(),sg.Button('开启',key='锁定壁纸开'),sg.Button('关闭',key='锁定壁纸关')],
        [sg.Text('禁用浏览器上网'),sg.Push(),sg.Button('开启',key='禁用浏览器上网开'),sg.Button('关闭',key='禁用浏览器上网关')]
    ]
    Window = sg.Window('电教管理工具(Ver 1.0 By Moemu)',layout,font=('微软雅黑 10'),size=(500,500))
    while True:
        event,value = Window.Read()
        if event == sg.WIN_CLOSED:
            os._exit(0)
        elif event == '锁定壁纸开':
            WallPaperLock(1)
        elif event == '锁定壁纸关':
            WallPaperLock(0)
        elif event == '禁用浏览器上网开':
            WebBrowserLock(1)
        elif event == '禁用浏览器上网关':
            WebBrowserLock(0)

if __name__=='__main__':
    main()