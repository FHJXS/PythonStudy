#导入socket库
import socket
import threading

import chardet
import time


def ClientFunc():
    """
    创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指
    定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket
    对象就创建成功，但是还没有建立连接。
    :return:
    """
    #创建一个Scoket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    s.connect(("www.sina.com.cn",80))
    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    print(chardet.detect(data)["encoding"])
    # print(type(chardet.detect(data)))
    # print(data.decode("utf-8"))
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('sina.html', 'wb') as f:
        f.write(html)

def ServiceFunc():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #监听端口
    s.bind(("127.0.0.1",9999))
    #调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
    s.listen(5)
    print("开始监听端口活动...")
    #服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        try:
            data = sock.recv(1024)
        except:
            data = b"Hello"
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

def ClientDemo2():
    """
    一个客户端
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

def UDPClientFunc():
    """
    使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
    虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
    我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口：
    :return:
    """
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定端口:
    s.bind(('127.0.0.1', 9999))
    #创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
    print('Bind UDP on 9999...')
    while True:
        # 接收数据:recvfrom()方法返回数据和客户端的地址与端口，这样
        # ，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s!' % data, addr)

def UDPServiceFunc():
    """
    客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.sendto(data, ('127.0.0.1', 9999))
        # 接收数据:
        print(s.recv(1024).decode('utf-8'))
    s.close()

if __name__ == '__main__':
    # ClientFunc()
    # ServiceFunc()
    # ClientDemo2()
    # UDPClientFunc()
    UDPServiceFunc()