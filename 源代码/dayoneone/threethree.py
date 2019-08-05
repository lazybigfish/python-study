#爬取QQ音乐周杰伦歌单

#单页版本
import requests

# url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=56802170905668863&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=467115783&loginUin=1435311604&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
# #以上地址在浏览器f12中，寻找network的xhr选项，找到搜索的数据的header，并找到其中的general的request URL地址
# res_music = requests.get(url)
#
# musis_list = res_music.json()
# #将返回的对象（Jason数据），转换为列表或者字典
#
# jay_list = musis_list['data']['song']['list']
# #逐层获取数据
# print('当前最热周杰伦歌单')
#
# i = 0
# for music in jay_list:
#     i = i + 1
#     print('第%s首'%(i))
#     print('歌曲名称：',music['name'])
#     print('专辑名称：',music['album']['name'])
#     print('专辑时间：',music['time_public'])


#多页版本

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

for x in range(5):

    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 该参数封装为字典后续重复调用，达成翻页效果

    res = requests.get(url,params = params)

    songer_list = res.json()

    songers_list = songer_list['data']['song']['list']

    # print(songer_list)

    for music in songers_list:
        print('第%s页'%(x +1))
        print('歌曲名：',music['name'])
        print('专辑名称：',music['album']['name'])
