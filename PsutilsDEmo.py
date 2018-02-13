import psutil

if __name__ == '__main__':
    #查看cpu逻辑数量
    print(psutil.cpu_count())

    #查看cpu物理核心
    print(psutil.cpu_count(logical=False))

    #系统启动时间
    print(psutil.boot_time())

    #统计CPU的用户／系统／空闲时间：
    print(psutil.cpu_times())

    #top命令的CPU使用率，每秒刷新一次，累计10次：
    # for x in range(10):
    #     print(psutil.cpu_percent(interval=1, percpu=True))

    #使用psutil获取物理内存和交换内存信息，分别使用：
    print(psutil.virtual_memory())

    print(psutil.swap_memory())

    # 磁盘分区信息 文件格式是HFS，opts中包含rw表示可读写，journaled表示支持日志。
    print(psutil.disk_partitions())

    # 磁盘使用情况
    print(psutil.disk_usage('/'))

    #磁盘IO
    print(psutil.disk_io_counters())

    #psutil可以获取网络接口和网络连接信息：
    ## 获取网络读写字节／包的个数
    print(psutil.net_io_counters())

    # # 获取网络接口信息
    print(psutil.net_if_addrs())
    print("\t\t")
    # 获取网络接口状态
    print( psutil.net_if_stats())

    #要获取当前网络连接信息，使用net_connections()：
    print(psutil.net_connections())

    #获取进程信息  所有进程ID
    print(psutil.pids())

    #) # 获取指定进程ID=3776，其实就是当前Python交互环境
    p = psutil.Process(4220)
    # 进程名称
    print(p.name())
    # 进程exe路径
    print(p.exe())
    # 进程工作目录
    print(p.cwd())
    # 进程启动的命令行
    print(p.cmdline())
    # 父进程ID
    print(p.ppid() )
    ## 父进程
    print(p.parent())
    # 子进程列表
    print(p.children())
    # 进程状态
    print(p.status())
    # 进程用户名
    print(p.username())
    # 进程创建时间
    print(p.create_time())
    #进程终端
    print(p.terminal())
    # 进程使用的CPU时间
    print(p.cpu_times())
    # 进程使用的内存
    print(p.memory_info())
    # 进程打开的文件
    print( p.open_files())
    # 进程相关网络连接
    print(p.connections())
    # 进程的线程数量
    print( p.num_threads())
    # 所有线程信息
    print(p.threads())
    ## 进程环境变量
    print(p.environ())
    #结束进程
    print(p.terminate())

    #获取进程相关信息i
    print(psutil.test())

