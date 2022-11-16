import requests
from lxml import html
url = 'https://pic.netbian.com/4kyingshi/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=headers)
response.encoding = 'gbk'
page_text = response.text
#print(page_text)
etree = html.etree
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
#print(li_list)
for li in li_list:
    img = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    print(img)
    img_name = li.xpath('./a/b/text()')[0] + '.jpg'
    #print(img_name)
    #爬取每张图片，是二进制的数据,用content取
    img_data = requests.get(img).content
    #保存图片
    with open('./pic/'+img_name,'wb') as fp:
        fp.write(img_data)
        print('下载成功')