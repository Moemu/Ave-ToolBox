import ToolBox
import getopt,sys,os
from OtherTool import *

def Management(Toolname:str,Status=None) -> None:
    '''
    对工具进行管理的通用接口
    Toolname: 工具名
    Status: 状态
    '''
    if Toolname == '添加\更改密码':
        PasswordChange()
    elif Toolname == 'help':
        print('''
        用法: Ave-Tool.exe -t <Toolname> --Status <Enable/DisEnable> [[--Password] <Password>]
        -t 指定工具
        --Status 工具状态
        --Password 密码
        用法例:
        Ave-Tool.exe -t WallPaperLock --Status Enable --Password 123
        ''')
    elif Toolname == 'Toollist':
        print(['WallPaperLock','WebBrowserLock','SystemToolLock'])
    elif Toolname == '锁定壁纸开' or (Toolname == 'WallPaperLock' and Status == 'Enable'):
        ToolBox.WallPaperLock(1)
    elif Toolname == '锁定壁纸关' or (Toolname == 'WallPaperLock' and Status == 'DisEnable'):
        ToolBox.WallPaperLock(0)
    elif Toolname == '禁用浏览器上网开' or (Toolname == 'WebBrowserLock' and Status == 'Enable'):
        ToolBox.WebBrowserLock(1)
    elif Toolname == '禁用浏览器上网关' or (Toolname == 'WebBrowserLock' and Status == 'DisEnable'):
        ToolBox.WebBrowserLock(0)
    elif Toolname == '禁用系统工具开' or (Toolname == 'SystemToolLock' and Status == 'Enable'):
        ToolBox.SystemToolLock(1)
    elif Toolname == '禁用系统工具关' or (Toolname == 'SystemToolLock' and Status == 'DisEnable'):
        ToolBox.SystemToolLock(0)
    else:
        if not Status in ['Enable','DisEnable',None]:
            print('Status参数有误')
        else:
            print('无法找到该工具...')
    return None

def CommandPrompt():
    '''
    纯命令提示符界面
    '''
    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:',longopts= ['Status=','Password='])
        if not 'Password' in args:
            opts.append(('Password','None'))
        print('tool:',opts[0][1])
        if opts[0][1] =='Toollist' or opts[0][1] =='help':
            Management(opts[0][1])
            os._exit(0)
        print('Status:',opts[1][1])
        if not CheckPassword(opts[2][1]):
            print('密码错误')
            os._exit(0)
        else:
            print('正在执行...')
        return opts[0][1],opts[1][1]
    except:
        print('参数错误!!!')