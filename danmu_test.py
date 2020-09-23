# from bs4 import BeautifulSoup
import requests
import json
import pandas as pd


# 提取某一期的弹幕
def get_danmu(num1, num2, page):
    url = 'https://bullet-ws.hitv.com/bullet/2020/09/19/{}/{}/{}.json'
    danmuurl = url.format(num1, num2, page)
    res = requests.get(danmuurl)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    details = []
    for i in range(len(jd['data']['items'])):
        result = {}
        result['stype'] = num2
        result['id'] = jd['data']['items'][i]['id']
        try:
            result['uname'] = jd['data']['items'][i]['uname']
        except:
            result['uname'] = ''
        result['content'] = jd['data']['items'][i]['content']
        result['time'] = jd['data']['items'][i]['time']
        try:
            result['v2_up_count'] = jd['data']['items'][i]['v2_up_count']
        except:
            result['v2_up_count'] = ''
        details.append(result)

    return details


# 输入关键信息
def count_danmu():
    danmu_total = []
    num1 = input('第一个数字')
    num2 = input('第二个数字')
    page = int(input('输入总时长'))
    for i in range(page):
        danmu_total.extend(get_danmu(num1, num2, i))

    return danmu_total


def main():
    danmu_end = []
    for j in range(10):
        danmu_end.extend(count_danmu())
    df = pd.DataFrame(danmu_end)
    df.to_excel('danmu_0619.xlsx')


if __name__ == '__main__':
    main()
