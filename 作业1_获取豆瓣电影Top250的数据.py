import requests
from lxml import html

# UA伪装: 让爬虫对应的请求载体标识伪装成一款浏览器,将对应的User-Agent封装到字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
urls = []   # 列表用于存放网址，一共有10个网址
num = 9*25+1
for i in range(0, num, 25):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    urls.append(url)
#  定义一个字典变量，存储生成的json文件
    jsontext = {'top250':[]}
# 循环访问页面并解析页面，取属性值
for i in range(10):
    response = requests.get(urls[i], headers=headers)
    # 获取响应的数据，text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 实例化一个etree对象
    etree = html.etree
    # 把需要解析的页面数据加载到该对象中
    tree = etree.HTML(page_text)
    # 取属性值
    # 取每部电影的名称
    li_list1 = tree.xpath('//div[@class="hd"]/a/span[1]')
    # 取每部电影的评分
    li_list2 = tree.xpath('//div[@class="star"]/span[2]')
    # 取每部电影的评分人数
    li_list3 = tree.xpath('//div[@class="star"]/span[4]')
    # for i in range(len(li_list1)):
    #     print(li_list1[i].text+' '+li_list2[i].text+' '+li_list3[i].text)
    for i in range(len(li_list1)):
        jsontext['top250'].append({'title':li_list1[i].text, 'rating_num':li_list2[i].text,'people_num':li_list3[i].text})

# print(jsontext)
import json

# # 后面的参数是调整生成的json的格式
jsondata = json.dumps(jsontext,indent=4,separators=(',', ': '),ensure_ascii=False)
# 最后生成json文件
with open('top250.json','w',encoding='utf-8') as fp:
    fp.write(jsondata)
print('爬取结束')


