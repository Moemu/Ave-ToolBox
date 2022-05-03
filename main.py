'''
Audio Visual Education Committee tools(电教委员管理工具)
Made by Moemu
Ver: 1.0
Feture: 壁纸锁定, 禁止上网
'''
from CommandPrompt import *
from ToolBox import *
import PySimpleGUI as sg
import os,sys,ToolBox

sg.theme('Reddit')

def main():
    if sys.argv[1:] != []:
        Toolname,Status = CommandPrompt()
        Management(Toolname,Status)
        print('已完成所做的更改...')
        os._exit(0)
    if os.path.isfile(os.getenv('APPDATA')+r'\Ave-ToolBox\Password.txt'):
        layout = [
            [sg.Text('输入密码以继续')],
            [sg.Input(password_char='*')],
            [sg.Button('继续')]
        ]
        window = sg.Window('登录验证',layout,font=('微软雅黑 10'))
        event, value = window.Read()
        while True:
            if event == sg.WIN_CLOSED:
                os._exit(0)
            if CheckPassword(value[0]):
                sg.Popup('密码正确,您可以继续',font=('微软雅黑 10'))
                window.Close()
                break
            else:
                sg.Popup('密码错误,您可能不是管理员',font=('微软雅黑 10'))
                event, value = window.Read()
    layout = [
        [sg.Menu([['密码',['添加\更改密码']]])],
        [sg.Text('电教管理工具(Ver 1.1 By Moemu)',font=('微软雅黑 15'))],
        [sg.Text('注意: 请以管理员模式打开程序, 不然程序无法使用',text_color='red')],
        [sg.Text('锁定壁纸'),sg.Push(),sg.Button('开启',key='锁定壁纸开'),sg.Button('关闭',key='锁定壁纸关')],
        [sg.Text('禁用浏览器上网'),sg.Push(),sg.Button('开启',key='禁用浏览器上网开'),sg.Button('关闭',key='禁用浏览器上网关')]
    ]
    Window = sg.Window('电教管理工具(Ver 1.0 By Moemu)',layout,font=('微软雅黑 10'),size=(500,500))
    while True:
        event,value = Window.Read()
        if event == sg.WIN_CLOSED:
            os._exit(0)
        else:
            Management(event)

if __name__=='__main__':
    main()