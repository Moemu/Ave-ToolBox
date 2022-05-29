import psutil,os,json,time
from datetime import datetime

class Log:
    def Write_Log(Tag:str,Message:str):
        log = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S') + ' [{}] '.format(Tag) + Message + '\n'
        with open(os.getenv('APPDATA')+'\Ave-ToolBox\log.txt','a') as f:
            f.write(log)
        print(log)
        return None
    def Start():
        Log.Write_Log('系统启动','程序开始运行')
    def Check_Process():
        # 加载监控列表
        with open(os.getenv('APPDATA')+'\Ave-ToolBox\MonitorProgram.json','r',encoding='utf-8') as f:
            data = json.loads(f.read())
        Namelist,Taglist,ProcessList,DescribeList = [],[],[],[]
        RunningProcess,StartRunTime,RunningProcessName,RunningProcessTag,RunningProcessDes = [],[],[],[],[]
        for d in data:
            Namelist.append(data[d]['Name'])
            Taglist.append(data[d]['Tag'])
            ProcessList.append(data[d]['ProcessName'])
            DescribeList.append(data[d]['Describe'])
        while True:
            # 加载进程列表
            process_name = []
            pids = psutil.pids()
            for pid in pids:
                try:
                    p = psutil.Process(pid)
                    process_name.append(p.name())
                except:
                    pass
            # print(process_name)
            #判断程序运行
            for p in ProcessList:
                if p in process_name:
                    num = ProcessList.index(p)
                    Log.Write_Log('程序启动','检测到 {} {} 启动, {}'.format(Taglist[num],Namelist[num],DescribeList[num]))
                    #暂时移除已运行程序
                    RunningProcessName.append(Namelist[num])
                    RunningProcessTag.append(Taglist[num])
                    RunningProcessDes.append(DescribeList[num])
                    RunningProcess.append(ProcessList[num])
                    StartRunTime.append(datetime.now())
                    Namelist.remove(Namelist[num])
                    Taglist.remove(Taglist[num])
                    ProcessList.remove(ProcessList[num])
                    DescribeList.remove(DescribeList[num])
            #判断程序终止运行
            for p in RunningProcess:
                if p not in process_name:
                    num = RunningProcess.index(p)
                    stime = StartRunTime[num]
                    ntime = datetime.now()
                    difference = round((ntime - stime).total_seconds()/60)
                    Log.Write_Log('程序结束','检测到 {} {} 结束运行,共运行 {} 分钟'.format(RunningProcessTag[num],RunningProcessName[num],difference))
                    #恢复已移除程序
                    Namelist.append(RunningProcessName[num])
                    Taglist.append(RunningProcessTag[num])
                    ProcessList.append(RunningProcess[num])
                    DescribeList.append(RunningProcessDes[num])
                    RunningProcessName.remove(RunningProcessName[num])
                    RunningProcessTag.remove(RunningProcessTag[num])
                    RunningProcessDes.remove(RunningProcessDes[num])
                    RunningProcess.remove(RunningProcess[num])
                    StartRunTime.remove(StartRunTime[num])
            time.sleep(1)

if __name__ == '__main__':
    Log.Start()
    if os.path.isfile(os.getenv('APPDATA')+'\Ave-ToolBox\MonitorProgram.json'):
        Log.Check_Process()