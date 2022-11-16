import requests
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
kw = input('请输入一字关键词:')
data = {
    'kw': kw
}
response = requests.post(url,data=data,headers=headers)
dic = response.json()
print(dic)