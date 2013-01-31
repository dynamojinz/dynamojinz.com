---
title: ubuntu(12.04, x64)中mysql安装与字符集设置
date: 2013-01-31 22:17:06
tags: [configs, ubuntu, mysql, charset]
slug: intalling-setting-mysql-in-ubuntu
---
今天又在ubuntu中折腾了一遍mysql，整了1个多小时，效率不高啊。

其实以前也折腾过一遍，只记得默认字符集需要设置成utf8，否则按默认设置建库的时候，
字符集会成为latin1，处理中文的时候会出现乱码。百度了好几篇，所说的方法是在
/etc/my.cnf 中 [client] 与 [mysqld] 中各添加一段:

    default-character-set = utf8

发现设置以后，新版本的mysql启动不了，去掉[mysqld]段添加那句后运行正常，但是
server端默认的character-set还是latin1。

最后不得不承认，用百度去解决技术问题效率真的不高，在
[stackoverflow](http://stackoverflow.com) 中搜了一下，问题得到了解决。

好记性不如烂笔头，还是记下来的好。

** 0. 安装环境 **

Ubuntu 12.04 x64

** 1. Mysql 安装 **

输入以下命令安装mysql:

    $ sudo apt-get install mysql-server mysql-client

按照向导设置好root的密码即可。

** 2. 停止mysql **

    $ sudo service mysql stop

** 3. 设置默认字符集 **

在/etc/mysql/my.cnf中[client]段中添加以下设置：

    [client]
    default-character-set = utf8

在[mysqld]段添加如下设置:

    [mysqld]
    collation-server = utf8_unicode_ci
    init-connect='SET NAMES utf8'
    character-set-server = utf8

保存文件并退出。

** 4. 启动mysql **

    $ sudo service mysql start

    启动成功的话，应该类似这样的输出：

    mysql start/running, process 32551

** 5. 检查默认字符集设置 **

首先登录mysql客户端:

    $ mysql -u root -p

输入下列命令查看character-set:

    mysql> show variables like 'character%';

正确设置后的输出大致如下:

    +--------------------------+----------------------------+
    | Variable_name            | Value                      |
    +--------------------------+----------------------------+
    | character_set_client     | utf8                       |
    | character_set_connection | utf8                       |
    | character_set_database   | utf8                       |
    | character_set_filesystem | binary                     |
    | character_set_results    | utf8                       |
    | character_set_server     | utf8                       |
    | character_set_system     | utf8                       |
    | character_sets_dir       | /usr/share/mysql/charsets/ |
    +--------------------------+----------------------------+
    8 rows in set (0.00 sec)

再检查collation设置:

    mysql> show variables like 'collation%';

结果大致如下:

    +----------------------+-----------------+
    | Variable_name        | Value           |
    +----------------------+-----------------+
    | collation_connection | utf8_general_ci |
    | collation_database   | utf8_unicode_ci |
    | collation_server     | utf8_unicode_ci |
    +----------------------+-----------------+
    3 rows in set (0.01 sec)

到这里，打完收功。
