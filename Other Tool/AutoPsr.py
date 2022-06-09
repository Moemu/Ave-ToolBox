'''
自动执行psr(步骤记录器)
需要Config_AutoPsr.json指定开始时间的结束时间
'''
import os,json,time,threading
from subprocess import getstatusoutput as cmd
from datetime import datetime
from LogRecover import Log

def RunPsr():
    global LogFile
    LogFile = datetime.strftime(datetime.now(),'%Y-%m-%d %H-%M-%S') + '.zip'
    if not os.path.isdir(os.getenv('APPDATA') + '\Ave-Toolbox\PsrLog'):
        os.mkdir(os.getenv('APPDATA') + '\Ave-Toolbox\PsrLog')
    path = os.getenv('APPDATA') + '\Ave-Toolbox\PsrLog\\' + LogFile
    Log.Write_Log('开始记录','步骤记录器开始运行')
    cmd('psr /start /gui 0 /output "{}"'.format(path))

def ClosePsr():
    cmd('psr /stop')
    Log.Write_Log('记录结束','步骤记录器停止运行,日志将保存在 '+LogFile+' 中')
    return None

def AutoRun():
    NowTime = datetime.now()
    NowYmd = datetime.strftime(NowTime,'%Y-%m-%d ')
    with open(os.getenv('APPDATA') + '\Ave-Toolbox\Config_AutoPsr.json','r') as f:
        data = f.read()
    data = json.loads(data)
    StartTime = NowYmd + data['StartTime']
    EndTime = NowYmd + data['EndTime']
    StartTime = datetime.strptime(StartTime,'%Y-%m-%d %H:%M')
    EndTime = datetime.strptime(EndTime,'%Y-%m-%d %H:%M')
    t1 = threading.Thread(target=RunPsr)
    t2 = threading.Thread(target=ClosePsr)
    while True:
        NowTime = datetime.now()
        if StartTime < NowTime < EndTime:
            t1.start()
            while True:
                NowTime = datetime.now()
                if NowTime > EndTime:
                    t2.start()
                    break
                time.sleep(60)
        time.sleep(60)

if __name__ == '__main__':
    AutoRun()