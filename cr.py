import requests
from bs4 import BeautifulSoup
import lxml
import xlrd,xlwt

rooturl = 'https://seo.chinaz.com/'
xlspath = 'testurl.xlsx'

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
    soup = BeautifulSoup(html.text, 'lxml')
    citename = soup.find(class_="_chinaz-seo-t2l").text
    # h = soup.find('title')

    # print (requests.utils.get_encoding_from_headers(headers))
    return citename

def create_url(urllist, sheetname, filename):
    # book = xlrd.open_workbook('testurl.xlsx')
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet(sheetname)
    for i in range(len(urllist)):
        worksheet.write(i,0,urllist[i])
    workbook.save(filename+'.xlsx') 
        

if __name__ == "__main__":
    # ,'advamed.org','haymancapital.com','lr.org','mckinsey.com','mitre.org','nacdl.org','npr.org'
    urllist = ['rolandberger.com','advamed.org','haymancapital.com','lr.org','mckinsey.com','mitre.org','nacdl.org','npr.org','chevron.com','cru.org','delta.com','fhi360.org','halfaker.com']
    create_url(urllist,'testur','testt')

    # for url in urllist:
    #     name = get_one_page(url)
    #     if len(name)!=1:
    #         print(url, '---->', name, len(name))
    #     else:
    #         print(url, '----> 需要手动获取信息')
