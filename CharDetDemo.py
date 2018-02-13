import chardet


def func():
    """
    可以进行编码检测
    :return:
    """
    print(chardet.detect(b"HelloWorld!"))

    data = "我是中国人，I'AM CHINESE!".encode("GBK")
    print(chardet.detect(data))

if __name__ == '__main__':
    func()
