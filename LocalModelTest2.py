# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import time

# Download the RSS feed and parse it
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def parseXml(URL):
    #解析为dom树结构
    rss = parse(urlopen(URL)).getroot()
    print(type(rss))

    location = {}
    data = {}
    forecast = []

    elment = rss.find('results/channel/{'+'{0}'.format(WEATHER_NS)+'}location')
    # #['__repr__', '__getattribute__', '__init__', '__len__', '__getitem__', '__setitem__',
    # '__delitem__', '__new__', 'clear', 'get', 'set', 'find', 'findtext', 'findall', 'append',
    # 'extend', 'insert', 'remove', 'iter', 'itertext', 'iterfind', 'getiterator', 'getchildren',
    # 'items', 'keys', 'makeelement', '__copy__', '__deepcopy__', '__sizeof__', '__getstate__',
    # '__setstate__', 'tag', 'text', 'tail', 'attrib', '__doc__', '__hash__', '__str__', '__setattr__',
    #  '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__',
    #  '__subclasshook__', '__init_subclass__', '__format__', '__dir__', '__class__']
    # print(elment.__dir__())
    location['city'] = elment.get('city')

    elment = rss.findall('results/channel/item/{'+'{0}'.format(WEATHER_NS)+'}forecast')
    for x in elment:
        data['date'] = time.strftime('%Y-%m-%d',time.strptime(x.get('date'),'%d %b %Y'))
        data['high'] = x.get('high')
        data['low'] = x.get('low')
        forecast.append(data)
    return {'city': location['city'],
            'forecast': forecast}

def demo01():
    result = parseXml(URL)
    print(result)
    assert result['city'] == 'Beijing'
    print('ok')

if __name__ == '__main__':
    # demo01()#案例查询天气
    pass