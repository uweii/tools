import time
import uuid

import simplejson
import requests as requests


registUrl = 'https://j03.space/signup'
loginUrl = 'https://j03.space/signin'
linkUrl = 'https://j03.space/xiaoma/copy_diy_class_link'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    "Accept-Encoding":"gzip",
    "Origin":"https://j03.space",
    "Referer":"https://t.cn/A6zPkxwO"

}


def register(email, name, password):
    body = {
        'email': email,
        'name': name,
        'passwd': password,
        'repasswd': password
    }
    res = requests.post(url=registUrl, data=body, headers=headers)
    return res


def login(email, password):
    body = {'email': email, 'passwd': password}
    res = requests.post(url=loginUrl, data=body,headers=headers)
    if res.status_code == 200:
        # getResult(res)
        return res



def getResult(res):
    if res.status_code == 200:
        cookies_dict = requests.utils.dict_from_cookiejar(res.cookies)
        # print(cookies_dict)
        link = requests.post(url=linkUrl,headers=headers, cookies=cookies_dict)
        print(link.text)
        jre = simplejson.loads(link.text)
        preLink = jre['data']['link']
        tab = jre['data']['tab']
        ssr = '不存在'
        clash = '不存在'
        V2ray = '不存在'
        trojan = '不存在'
        for i in tab:
            if i['name'] == 'SSR':
                ssr = i['link']
                continue
            if i['name'] == 'clash':
                clash = i['link']
                continue
            if i['name'] == 'V2ray':
                V2ray = i['link']
                continue
            if i['name'] == 'trojan':
                trojan = i['link']
        print("ssr: {}".format(preLink + ssr))
        print("clash: {}".format(preLink + clash))
        print("V2ray: {}".format(preLink + V2ray))
        print("trojan: {}".format(preLink + trojan))



def mainPid(email, name, password):
    registResult = register(email, name, password)
    print(registResult.text.encode().decode('unicode_escape'))
    if registResult.status_code == 200:
        print("注册成功：用户名{}, 密码{}".format(email, password))
        loginRes = login(email, password)
        print(loginRes.text.encode().decode('unicode_escape'))
    else:
        print("注册失败")
    if loginRes.status_code == 200:
            getResult(loginRes)
    else:
        print("登录失败")

# 邮箱
register_email = '{}'.format(time.time())
# 用户名
register_name = '1'
# 密码
register_password = '12345678'

if __name__ == '__main__':
    mainPid(register_email, register_name, register_password)
    # login(register_email, register_password)


