'''
此类用于存放各工具源码
'''
import subprocess,shutil
from OtherTool import *

def Creat_Config_File():
    '''
    新建配置文件
    '''
    import json
    layout = [
        [sg.Text('此向导将引导您新建配置文件以在一台全新的系统上快速配置')],
        [sg.Text('壁纸锁定:'),sg.Checkbox('开启')],
        [sg.Text('禁用系统工具'),sg.Checkbox('开启')],
        [sg.Text('禁用浏览器'),sg.Checkbox('开启')],
        [sg.Text('Ave-Toolbox密码:'),sg.Input()],
        [sg.Button('提交')]
    ]
    window = sg.Window('新建配置文件',layout,font=('微软雅黑 10'))
    event,value = window.read()
    if event == sg.WIN_CLOSED:
        window.Close()
        return None
    print(value)
    WallPaperLock = value[0]
    SystemToolLock = value[1]
    BrowserLock = value[2]
    Password = value[3]
    with open('Config.json','w') as f:
        f.write(json.dumps({'WallPaperLock':WallPaperLock,'SystemToolLock':SystemToolLock,'BrowserLock':BrowserLock,'Password':Password}))
    sg.Popup('配置文件(Config.json)已保存',title='完成',font=('微软雅黑 10'))
    window.Close()
    return None

def Load_Config_File():
    import json
    layout = [
        [sg.Text('配置文件位置'),sg.Input(),sg.FileBrowse('打开')],
        [sg.Button('导入')]
    ]
    window = sg.Window('载入配置文件',layout,font=('微软雅黑 10'))
    event,value = window.Read()
    Config_Path = value[0]
    if event == sg.WIN_CLOSED:
        window.Close()
        return None
    elif not os.path.isfile(Config_Path):
        sg.Popup('该路径没有任何文件!',title='错误',font=('微软雅黑 10'))
    with open(Config_Path,'r') as f:
        Config = f.read()
    Config = json.loads(Config)
    if Config['WallPaperPath'] != '':
        SetWallpaper(Config['WallPaperPath'])
    if Config['WallPaperLock'] == True:
        WallPaperLock(1)
    if Config['SystemToolLock'] == True:
        SystemToolLock(1)
    if Config['BrowserLock'] == True:
        WebBrowserLock(1)
    if Config['Password'] != '':
        AddPassword(Config['Password'])
    return None

def Install_AveService():
    '''
    初次启动时写入启动信息
    '''
    if not os.path.isdir(os.getenv('APPDATA')+'\Ave-ToolBox'):
        os.mkdir(os.getenv('APPDATA')+'\Ave-ToolBox')
    shutil.copyfile('BackStage.exe',os.getenv('APPDATA')+'\Ave-ToolBox\BackStage.exe')
    WriteValue(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\Windows\CurrentVersion\Run','BackStageOfAve',win32con.REG_SZ,os.getenv('APPDATA')+'\Ave-ToolBox\BackStage.exe')
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

def SystemToolLock(Status:int):
    '''
    系统工具锁
    '''
    WriteValue(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system','DisableTaskmgr',win32con.REG_DWORD,Status)
    WriteValue(win32con.HKEY_CURRENT_USER,'software\microsoft\windows\currentVersion\policies\system','DisableRegistryTools',win32con.REG_DWORD,Status)
    WriteValue(win32con.HKEY_CURRENT_USER,'SOFTWARE\Policies\Microsoft\Windows\System','DisableCMD',win32con.REG_DWORD,Status)
    WriteValue(win32con.HKEY_CURRENT_USER,'SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\EXPLORER','RESTRICTRUN',win32con.REG_DWORD,Status)