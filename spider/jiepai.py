
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
from json import JSONDecodeError
from bs4 import BeautifulSoup
import re

def get_page_index(offset,keyword):
    data = {
        'aid': 24,
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
    }
    url = "https://www.toutiao.com/api/search/content/?" + urlencode(data)
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None


def parse_page_index(html):
    data = json.loads(html)
    try:
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        print('解析索引页出错')
        return None

def get_page_detail(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException:
        print('请求详情页出错')
        return None
#
# def parse_page_detail(html,url):
#     soup = BeautifulSoup(html,'lxml')
#     title = soup.select('title')[0].get_text()
#     print(title)
#     images_pattern = re.compile('BASE_DATA.galleryInfo.*?gallery: JSON.parse.*?"(.*?)"\),',re.S)
#     result = re.search(images_pattern,html)
#     if result:
#         data = json.loads(result.group(1))
#         if data and 'sub_images' in data.keys():
#             sub_images = data.get('sub_images')
#             images = [item.get('url') for item in sub_images]
#             return {
#                 'title': title,
#                 'url': url,
#                 'images': images
#             }

def parse_page_detail(html, url):
    images_pattern = re.compile(r'BASE_DATA.galleryInfo.*?gallery: JSON.parse.*?"(.*?)"\),', re.S)
    result = re.search(images_pattern, html)
    if result != None:
        soup = BeautifulSoup(html, 'lxml')
        title = soup.select('title')[0].get_text()
        data = re.sub('\\\\"', '"', result.group(1))
        data = re.sub(r'\\\\', '', data)
        data = json.loads(data)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
                'title': title,
                'url': url,
                'images': images
            }
def main():
    html = get_page_index(0,'街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            print(result)

if __name__ == '__main__':
    main()

