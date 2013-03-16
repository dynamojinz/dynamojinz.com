---
title: 2013-03-16-upgrade-git
date: 2013-03-16 22:12:02
tags: [configs, ubuntu, git]
slug: upgrade-git
---
这个故事说来有点曲折:

本来的目的是想整理我的简历，于是为了整简历新建了一个Git项目放到github上

结果git push不上去，查了下官方的帮助，建议我先把Git升级到1.7.10以上

于是乎我检查了Git版本，还是1.7.9,运行：

	sudo apt-get install git
	正在读取软件包列表... 完成
	正在分析软件包的依赖关系树       
	正在读取状态信息... 完成       
	git 已经是最新的版本了。

明显我的ubuntu源里没有更新的Git版本，于是Google之，在咖啡兔(http://www.kafeitu.me/)
的博客上找到了解决方案：

	sudo apt-add-repository ppa:git-core/ppa
	sudo apt-get update
	sudo apt-get install git

这么一番折腾以后，Git倒是升级到1.8.2了，项目还是Push不上去，结果新开了个Terminal，又顺利Push上了

哎，附带的好处就是添加了最近Git的源了
