'''
其他工具(非直接调用)
'''
import os,hashlib,win32api,win32con
import PySimpleGUI as sg

def CreatKey(Rootdirectory=None,Path:str=None,Keyname:str=None):
    '''
    在注册表中新建项
    Rootdirectory: 注册表第一层目录
    Path: 注册表下层路径
    Keyname: 项名
    '''
    key = win32api.RegOpenKey(Rootdirectory,Path,0, win32con.KEY_ALL_ACCESS)
    win32api.RegCreateKey(key,Keyname)
    return None

def WriteValue(Rootdirectory=None,Path:str=None,Keyname:str=None,Keytype=None,Keyvalue:str=None):
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

def SetWallpaper(Path):
    '''
    设置壁纸
    '''
    CreatKey(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Policies','System')
    WriteValue(win32con.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Policies\System','Wallpaper',win32con.REG_SZ,Path)
    return None

def CheckPassword(Password:str) -> bool:
    '''
    密码检测
    Password: 密码
    '''
    if os.path.isfile(os.getenv('APPDATA')+r'\Ave-ToolBox\Password.txt'):
        with open(os.getenv('APPDATA')+r'\Ave-ToolBox\Password.txt') as f:
            if f.read() == hashlib.md5(Password.encode('utf-8')).hexdigest():
                return True
            else:
                return False
    else:
        return True

def AddPassword(Password:str) -> None:
    '''
    密码添加服务
    Password: 密码
    '''
    if not os.path.isdir(os.getenv('APPDATA')+r'\Ave-ToolBox'):
        os.mkdir(os.getenv('APPDATA')+r'\Ave-ToolBox')
    with open(os.getenv('APPDATA')+r'\Ave-ToolBox\Password.txt','w') as f:
        f.write(hashlib.md5(Password.encode('utf-8')).hexdigest())
    return None

def PasswordChange() -> None:
    '''
    密码更改
    '''
    layout = [
        [sg.Text('输入新的密码:')],
        [sg.Input(password_char='*')],
        [sg.Text('再次输入密码:')],
        [sg.Input(password_char='*')],
        [sg.Button('提交')]
    ]
    Window = sg.Window('添加\更改密码',layout=layout,size=(400,180),font=('微软雅黑 10'))
    event, value = Window.Read()
    if event == sg.WIN_CLOSED:
        return None
    if value[0] != value[1] or value[0] == '':
        sg.Popup('两次输入密码不同/不能为空',font=('微软雅黑 10'))
        return None
    AddPassword(value[0])
    sg.Popup('添加成功...',font=('微软雅黑 10'))
    Window.Close()
    return None