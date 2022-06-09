import os,win32api,win32con,shutil

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

def Install_LogRecover():
    '''
    初次启动时写入启动信息
    '''
    if not os.path.isdir(os.getenv('APPDATA')+'\Ave-ToolBox'):
        os.mkdir(os.getenv('APPDATA')+'\Ave-ToolBox')
    shutil.copyfile('BackStage.exe',os.getenv('APPDATA')+'\Ave-ToolBox\BackStage.exe')
    WriteValue(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\Windows\CurrentVersion\Run','BackStageOfAve',win32con.REG_SZ,os.getenv('APPDATA')+'\Ave-ToolBox\BackStage.exe')
    return None

def Install_AutoPsr():
    '''
    AutoPsr注册服务
    '''
    if not os.path.isdir(os.getenv('APPDATA')+'\Ave-ToolBox\PsrLog'):
        os.mkdir(os.getenv('APPDATA')+'\Ave-ToolBox\PsrLog')
    shutil.copyfile('AutoPsr.exe',os.getenv('APPDATA')+'\Ave-ToolBox\AutoPsr.exe')
    WriteValue(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\Windows\CurrentVersion\Run','AutoPsr',win32con.REG_SZ,os.getenv('APPDATA')+'\Ave-ToolBox\AutoPsr.exe')
    return None

if __name__ == '__main__':
    Install_LogRecover()
    Install_AutoPsr()