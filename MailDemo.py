import poplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.parser import Parser
from email.utils import parseaddr, formataddr
from email.header import decode_header
import smtplib

import io


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def SMTPFunc():
    """
    我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，
    sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
    邮件正文是一个str，as_string()把MIMEText对象变成str。
    :return:
    """

    # 输入Email地址和口令:
    from_addr ="www.609446687@qq.com" #input('From: ')
    password ="akftotzevngxbcje" #input('Password: ')
    #输入收件人服务器
    to_addr ="a609446687@163.com" #input('To: ')
    # 输入SMTP服务器地址:
    smtp_server = "smtp.qq.com"#input('SMTP server: ')
    #构造一个最简单的纯文本邮件：
    msg = MIMEText("你好，发送来自Python测试...","plain","utf-8")#MIMEMultipart() #
    #添加邮件没有主题；
    #收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
    #明明收到了邮件，却提示不在收件人中。
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    # msg.preamble = "你好，发送来自Python测试..."
    # # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    # with open('福.jpg', 'rb') as f:
    #     # 设置附件的MIME和文件名，这里是png类型:
    #     mime = MIMEBase('image', 'JPG', filename='新年福到.png')
    #     # f = io.StringIO('新年福到.png')
    #     # mime = MIMEText(f.getvalue())
    #     # 加上必要的头信息:
    #     mime.add_header('Content-Disposition', 'attachment', filename='新年福到.png')
    #     mime.add_header('Content-ID', '<0>')
    #     mime.add_header('X-Attachment-Id', '0')
    #     # 把附件的内容读进来:
    #     mime.set_payload(f.read())
    #     # 用Base64编码:
    #     encoders.encode_base64(mime)
    #     # 添加到MIMEMultipart:
    #     msg.attach(mime)

    # server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server = smtplib.SMTP_SSL(smtp_server, 465)  # 需要使用这种方式发送
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def SMTPDemo2():
    # 输入Email地址和口令:
    from_addr = "www.609446687@qq.com"  # input('From: ')
    password = "akftotzevngxbcje"  # input('Password: ')
    # 输入收件人服务器
    to_addr = "a609446687@163.com"  # input('To: ')
    # 输入SMTP服务器地址:
    smtp_server = "smtp.qq.com"  # input('SMTP server: ')

    msg = MIMEMultipart('alternative')
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    msg.attach(MIMEText('hello', 'plain', 'utf-8'))
    msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

    # server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server = smtplib.SMTP_SSL(smtp_server, 465) #需要使用这种方式发送
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

"""
使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，
正确设置好邮件头，就可以顺利发出。
构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一
个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要
把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象
。它们的继承关系如下：
    Message
    +- MIMEBase
       +- MIMEMultipart
       +- MIMENonMultipart
          +- MIMEMessage
          +- MIMEText
          +- MIMEImage
"""

def POP3Func():
    """
    收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。
    Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。
    所以，收取邮件分两步：
        第一步：用poplib把邮件的原始文本下载到本地；
        第二部：用email解析原始文本，还原为邮件对象。
    :return:
    """
    # 输入邮件地址, 口令和POP3服务器地址:
    email = "www.609446687@qq.com"##input('Email: ')
    password = "akftotzevngxbcje"#input('Password: ')
    pop3_server ="pop.qq.com"# input('POP3 server: ')
    # 连接到POP3服务器:
    # server = poplib.POP3(pop3_server)
    server = poplib.POP3_SSL(pop3_server)
    # 可以打开或关闭调试信息:
    server.set_debuglevel(1)
    # 可选:打印POP3服务器的欢迎文字:
    print(server.getwelcome().decode('utf-8'))

    # 身份认证:
    server.user(email)
    server.pass_(password)

    # stat()返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)

    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    print_info(msg)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()

# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

def decode_str(s):
    """
    邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
    :param s:
    :return:
    """
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    """
    decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。
    文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
    :param msg:
    :return:
    """
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
if __name__ == '__main__':
    POP3Func()