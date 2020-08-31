import urllib.request
import urllib.error
import urllib.parse
import socket

headers = {'Accept': 'text/javascript, application/javascript, application/ecmascript,'
                     ' application/x-ecmascript, */*; q=0.01',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36'}
value = {"phone":'15032373556',
         "password":'ljy1997'}
proxy = {'http':'218.58.194.162'}
timeout = 2
try:
    socket.setdefaulttimeout(timeout)
    data = urllib.parse.urlencode(value).encode('utf-8')
    response = urllib.request.Request('https://www.douban.com/',data=data,headers=headers)
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    html = opener.open(response)
    result = html.read().decode('utf-8')
    print(result)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误状态码是' + str(e.code))
except socket.timeout:
    print('socket超时')
else:
    print('请求成功通过。')
