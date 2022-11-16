import requests
from lxml import html
import os
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=headers)
page_text = response.json()
#print(page_text)
if not os.path.exists('./lol'):
    os.makedirs('./lol')
hero_list = page_text['hero']
#print(hero_list)
for hero in hero_list:
    print(hero)
    path = './lol/'+hero['name'] + '/'
    os.makedirs(path)
    audio = requests.get(hero['selectAudio'],headers=headers).content
    #取文件名
    name = hero['selectAudio'].split('/')[-1]
    #print(name)
    with open(path+name,'wb') as fp:
        fp.write(audio)
        print('下载完成')