---
title: 在Win7中与手机共享网络连接
date: 2013-01-30 12:07:13
tags: [configs, windows]
slug: share-connection-with-mobiles
---
今天在没有Wifi信号的地方用笔记本有线上网，突然想着让手机也共享一下网络。结果却发现
Win7自带的创建临时网络功能，只能支持计算机到计算机的共享，不能带着手机上网。俗话说
内事不决问老婆，外事不决问百度，百度之后发现Win7还是支持承载Wifi热点的，只不过需要
在命令行状态下手动设置：

** 1. 启用“虚拟Wifi网络”功能 **

以管理员身份运行cmd，输入下列命令启用虚拟Wifi网络:

	netsh wlan set hostednetwork mode=allow ssid=[your-ssid] key=[your-key]

其中[your-ssid]为设置的Wifi网络名，[your-key]为相应的密钥。

** 2. 开启虚拟Wifi **

在cmd中再输入以下命令开启虚拟Wifi:

	netsh wlan start hostednetwork

这时可以看见，在网络共享中心中，“无线网络连接2”已经启用了，还需要将有线上网的连接
共享给“无线网络连接2”，以实现共享上网。

这时打开手机Wifi，搜索上面设置的ssid，输入密钥连接Wifi就可以共享上网了

** 3. 其它设置 **

相应的，关闭Wifi共享的命令为:

	netsh wlan stop hostednetwork

卸载虚拟Wifi的命令为:

	netsh wlan set hostednetwork mode=disallow

查看虚拟Wifi设置的命令为:

	netsh wlan show hostednetwork

关机的同时，Wifi共享也会关闭，为了使用的便利，我将Start和Stop的命令保存
为.bat文件放在桌面上，需要用的时候，右击相应的文件选择“以管理员身份运行”
就可以了。

