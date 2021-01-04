import requests
from bs4 import BeautifulSoup
import lxml

rooturl = 'https://seo.chinaz.com/'

proxy = {
    'http': 'http://localhost:4780',
    'https': 'http://localhost:4780'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def get_one_page(url):
    url = rooturl+url
    # print(url)
    html = requests.get(url, headers=headers, proxies=proxy)
    # print(html.encoding)
    # html.encoding = "GB2312"
    # print(html.encoding)
    # html.encoding = html.apparent_encoding
    # html.content.decode('unicode')
    # html = html.content
    # html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
    # x = requests.utils.get_encoding_from_headers(html.text)
    # print(html.content.decode(html.encoding))
    soup = BeautifulSoup(html.text, 'lxml')
    h = soup.find(class_="_chinaz-seo-t2l").text
    # h = soup.find('title')

    # print (requests.utils.get_encoding_from_headers(headers))
    return h


if __name__ == "__main__":
    # ,'advamed.org','haymancapital.com','lr.org','mckinsey.com','mitre.org','nacdl.org','npr.org'
    urllist = ['rolandberger.com','advamed.org','haymancapital.com','lr.org','mckinsey.com','mitre.org','nacdl.org','npr.org','chevron.com','cru.org','delta.com','fhi360.org','halfaker.com']
    for url in urllist:
        name = get_one_page(url)
        if name:
            print(url, '---->', name)
        else:
            print(url, '----> 未找到详细信息')
