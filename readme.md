# Ave-ToolBox（电教管理工具）

电教管理工具，让别的学生不能占用你使用一体机的宝贵机会，同时还能赢得班主任的赞誉。

# 注意事项

1. 即使你不是电教也可以通过该程序限制电教的使用（当然前提你得不被发现）
2. 本程序完全开源，如果你们班的电教通过该程序限制了某些功能，那么你也可以改回来
3. EXE运行环境为**Windows 10 64位以上**，如果你们用的是Windows 7及以下，那么你可以装Windows 10或者劝电教装。
4. 你需要以管理员权限运行该程序

# 功能与原理

## 锁定壁纸

修改注册表:

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop
```

下的项"NochangingWallpaper"为1，防止为允许更改壁纸

## 禁用浏览器上网

使用netsh添加防火墙连接规则：

```
netsh advfirewall firewall add rule name="WebBrowserLock1" dir=out program="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" action=block
```

重启用方式：

```
Netsh advfirewall firewall set rule name="WebBrowserLock1" new enable=no
```

考虑到作者的实际情况，目前仅添加了默认路径下的Microsoft Edge，如果还想添加更多浏览器的支持，还请各位提交PR

# Feature:

- [ ] 1. 禁止安装软件
- [ ] 2. 启动密码验证