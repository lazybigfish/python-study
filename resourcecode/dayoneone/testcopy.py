import requests,bs4

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.jobui.com/rank/company/'

res = requests.get(url,headers= headers)

soup = bs4.BeautifulSoup(res.text,'html.parser')

bs = soup.find_all('ul',class_='textList flsty cfix')

print(bs)

