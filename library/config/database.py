# coding:utf-8
redis_config = {
    'default' : {
        'host' : '127.0.0.1',
        # IP地址
        'port' : 6379,
        # 端口
        'db' : 0,
        # 数据库名
        'max_connections' : 100,
        # 最大连接数
        'pwd' : 'cyz@2018sdut',
        # 如果密码为空，None
        'type' : 'default',
        # 读写模式
    },
    'session' : {
        'host' : '127.0.0.1',
        'port' : 6379,
        'db' : 0,
        'max_connections' : 100,
        'pwd' : 'cyz@2018sdut',
        # 如果密码为空，None
        'type' : 'default',
        # 读写模式
        'prefix' : 'devops_session'
    },
    'socket_timeout' : None,
    'socket_connect_timeout' : None,
    'socket_keepalive' : 90,
}

mongo_config = {
    'default' : {
        'host' : 'localhost',
        # IP地址
        'port' : 27017,
        # 端口
        'db' : 'devops',
        # 数据库名
        'user' : 'devops',
        # 连接用户名
        'pwd' : 'cyz@2018sdut',
        # 连接密码
        'type' : 'default',
        # 读写模式
    },
    # 默认连接方式。暂时本系统除了ansible的callback模块外，均使用该连接方式
    'log' : {
        'host' : 'localhost',
        'port' : 27017,
        'db' : 'devops',
        'user' : 'devops',
        'pwd' : 'cyz@2018sdut',
        'type' : 'default',
    },
    # 暂时本系统只有ansible的callback模块在使用
    'mechanism':"SCRAM-SHA-1"
}

