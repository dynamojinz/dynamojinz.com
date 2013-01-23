---
title: 使用Acrylamid创建静态博客
date: 2013-01-21 14:34:25
tags: configs
---
在[greatghoul](http://github.com/greatghoul)的推荐下，用[Acrylamid](http://github.com/posativ/acrylamid)
作为博客引擎，建立了这个静态博客程序。

建站过程具体参考[Acrylamid](http://github.com/posativ/acrylamid)的主页，我在这里主要做了一点更改：

** 1.用virtualenv在blog目录下建立了venv目录，并安装[Acrylamid](http://github.com/posativ/acrylamid) **

    $ mkdir dynamojinz.com
    $ cd dynamojinz.com
    $ virtualenv venv
    $ . venv/bin/activate

** 2.建立git仓库，编缉.gitignore文件，忽略以下的文件项: **

    /venv
    /output
    /.cache

** 3.更改默认的theme，用[Bootstrap](http://github.com/twitter/Bootstrap)作为网页的样式。 **

** 4.注册Disqus作为评论功能的支持: **

作者没有提到的是，Acrylamid中已经默认支持了Disqus，只需要在conf.py中设置：

	DISQUS_SHORTNAME = 'your_disqus_shorname'

** 5.目前在[Amazon](http://aws.amazon.com/ec2)的ec2云计算平台中注册了一个VPS作为博客的Host(一年免费)**

在conf.py中作以下设置来启用Acrylamid的Deploy功能：

	DEPLOYMENT = {
		"ls": "ls $OUTPUT_DIR",
		"echo": "echo $OUTPUT_DIR",
		"default": "rsync -avz --delete $OUTPUT_DIR ec2-user@your_instance_ip:/var/www/html/",
	}

这样用以下命令编译博客，并同步生成的博客内容到服务器上：

	$ acrylamid compile
	$ acrylamid deploy

