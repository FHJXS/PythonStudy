import requests


def func01():
    """
    可以直接通过get请求访问一个页面
    :return:
    """
    r = requests.get('https://www.douban.com/')  # 豆瓣首页
    print(r.status_code)
    # print(r.text)


def func02():
    """
    也可以直接带参传入 dict
    :return:
    """
    # r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
    r = requests.get("http://www.baidu.com/s", params={"wd": "Java资料"})
    # 查看实际请求的URL
    print(r.url)
    print(r.status_code)
    # 查看当前编码
    print(r.encoding)
    # 获得str
    # print(r.text)
    # 获得bytes对象：
    # print(r.content)
    # JSON，可以直接获取
    # print(r.json())

    # 需要传入HTTP Header时，我们传入一个dict作为headers参数：
    r1 = requests.get('https://www.douban.com/',
                      headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    # print(r1.text)
    print(r1.encoding)

    # 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
    r2 = requests.post('https://accounts.douban.com/login',
                       data={'form_email': 'abc@example.com', 'form_password': '123456'})
    #requests对获取HTTP响应的其他信息也非常简单
    print(r2.headers["Date"])

    # requests默认使用application/x-www-form-urlencoded对POST数据编码。
    # 如果要传递JSON数据，可以直接传入json参数
    # params = {'key': 'value'}
    # r = requests.post(url, json=params)  # 内部自动序列化为JSON

    # 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
    # 在读取文件时，注意务必使用 'rb'
    # 即二进制模式读取，这样获取的bytes长度才是文件的长度。
    # 把post()方法替换为put()，delete()
    # 等，就可以以PUT或DELETE方式请求资源。
    # upload_files = {'file': open('report.xls', 'rb')}
    # r = requests.post("上传地址", files=upload_files)

    #requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的
    print(r.cookies["BIDUPSID"])#<class 'requests.cookies.RequestsCookieJar'>

    #要在请求中传入Cookie，只需准备一个dict传入cookies参数：
    # cs = {'token': '12345', 'status': 'working'}
    # r = requests.get("请求地址", cookies=cs)
    #指定超时时间
    # r = requests.get(url, timeout=2.5)  # 2.5秒后超时

if __name__ == '__main__':
    func02()
