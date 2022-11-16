import requests
from lxml import html
import pymysql
import time
import random
# 不显示警告信息
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



name_list = []  # 房源名称列表
house_type_list = []  # 户型列表
area_list = []  # 面积列表
address_list = []  # 地址列表
price_list = []  # 价格
img_list = []  # 图片列表
year_list = []  # 取建造年份
# #获取数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='147abc', db='58city', charset='utf8')
# #获取数据库游标
cur = conn.cursor()
for i in range(0, 5):
    print(f'开始爬取第{i + 1}页')
    page = i + 1
    # 58同城二手房第一页
    url = f'https://zj.58.com/ershoufang/p{page}/?PGTID=0d200001-0028-51f4-2a1a-0d12e4b14744&ClickID=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                      'Connection':'close'
    }
    response = requests.get(url, headers=headers,verify=False)
    time.sleep(5 + random.random() * 3)  # 设置访问网址间隔时间
    page_text = response.text
    # print(page_text)
    etree = html.etree
    tree = etree.HTML(page_text)
    # 获取所有的二手房
    li_list = tree.xpath('//div[@class="property"]')
    # 遍历
    for li in li_list:
        # 取房源名称
        name = li.xpath('./a/div[@class="property-content"]/div[@class="property-content-detail"]/div['
                        '@class="property-content-title"]/h3/text()')[0]
        print(name)
        # 去除前后空格和换行
        name = name.replace('""', '').replace('\n', '').strip()
        # print(name)
        # 取户型
        house_type = li.xpath('./a/div[@class="property-content"]/div[@class="property-content-detail"]/section/'
                              'div[@class="property-content-info"]/p[@class="property-content-info-text '
                              'property-content-info-attribute"] '
                              '/span/text()')
        house_type = "".join(house_type)
        print(house_type)
        # 取面积
        area = li.xpath('./a/div[@class="property-content"]/div[@class="property-content-detail"]/section/'
                        'div[@class="property-content-info"]/p[@class="property-content-info-text"]/'
                        'text()')[0]
        # print(area)
        # 去除前后空格和换行
        area = area.replace('""', '').replace('\n', '').strip()
        # print(area)
        # 将面积转为浮点类型(去掉㎡)
        area = area[:-1]
        area = float(area)
        print(area)
        # 取地址
        # 小区名字
        residential = li.xpath('./a/div[@class="property-content"]/div[@class="property-content-detail"]/section/'
                               'div[@class="property-content-info property-content-info-comm"]/p['
                               '@class="property-content-info-comm-name"]/text()')[0]
        # print(residential)
        # 具体地址
        address = li.xpath('./a/div[@class="property-content"]/div[@class="property-content-detail"]/section/'
                           'div[@class="property-content-info property-content-info-comm"]/p['
                           '@class="property-content-info-comm-address"]/span/text()')
        address = "-".join(address)
        address = residential + '    ' + address
        print(address)
        # 取价格
        price = li.xpath('./a/div[@class="property-content"]/div[@class="property-price"]/p['
                         '@class="property-price-total"]/span[@class="property-price-total-num"]/text()')[0]
        print(price)
        # 房源详情页获取图片地址
        detail_url = li.xpath('./a/@href')[0]
        # print(detail_url)
        detail_text = requests.get(detail_url, headers=headers,verify=False).text
        time.sleep(5 + random.random() * 3)  # 设置访问网址间隔时间
        etree = html.etree
        tree = etree.HTML(detail_text)
        img = tree.xpath('//img[@class="gallery-indicator-image-item"]/@src')[0]
        print(img)
        # 取建造年份
        year = li.xpath('./a/div[2]/div[1]/section/div[1]/p[last()]/text()')[0]
        # print(year)
        # 去除前后空格和换行
        year = year.replace('""', '').replace('\n', '').strip()
        # 有的二手房没有建造年份，判断所获取数据是否是建造年份，如果不是，把建造年份改为0，如果是，将建造年份转为整型(去掉“年建造”)
        if '年建造' not in year:
            year = 0
        else:
            year = year[:-3]
            year = int(year)
        print(year)
        # 把每个房源的名称,户型,面积,地址,价格,图片、建造年份存入列表中
        name_list.append(name)
        house_type_list.append(house_type)
        area_list.append(area)
        address_list.append(address)
        price_list.append(price)
        img_list.append(img)
        year_list.append(year)
        # 插入数据库
        try:
            # 定义SQL语句
            sql = "insert into second_hand_house(name,house_type,area,address,price,photo,year) values(%s,%s,%s,%s,%s,%s,%s)"
            # 设置sql语句values中参数的值
            val = (name, house_type, area, address, price, img, year)
            # 执行sql语句
            cur.execute(sql, val)
            # 提交
            conn.commit()
            print('插入成功')
        except Exception as e:
            print(e)

# 创建字典数据
dict = {}
dict['房源名称'] = name_list
dict['户型'] = house_type_list
dict['面积'] = area_list
dict['地址'] = address_list
dict['价格'] = price_list
dict['图片'] = img_list
dict['建造年份'] = year_list
# print(dict)
# 构造DataFrame
import pandas as pd

df = pd.DataFrame(dict)
# print(df)
df.to_excel('58同城二手房信息.xlsx', index=False)
print('保存成功')
