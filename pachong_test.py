# coding:utf-8

# 引入相关模块
import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/"
headers = {
                'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            }

wbdata = requests.get(url,headers = headers).text
#print(wbdata.encode('utf-8'))

# 创建解析器
soup = BeautifulSoup(wbdata,'lxml')

#输出网页内容：注：此内容已被缩进格式化
#print(soup.prettify().encode('utf-8'))

#获取id属性值为billboard的元素节点
#news_titles = soup.select("#billboard")

#获取class属性为title的td元素里面所有的a元素节点
news_titles = soup.select("td.title a")
for n in news_titles:
    print(n.encode('utf-8'))

# 对返回的列表进行遍历
for n in news_titles:
    # 提取出标题和链接信息
    title = n.get_text()
    print(title.encode('utf-8'))
    link = n.get("href")
    print(link)
