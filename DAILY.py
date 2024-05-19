import requests
import os
import json


cookie_value = os.getenv('COOKIE')
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}


import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'dnt': '1',
    'origin': 'https://act.hoyolab.com',
    'priority': 'u=1, i',
    'referer': 'https://act.hoyolab.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-rpc-app_version': '',
    'x-rpc-device_id': '7eec8c61-38b9-4e9f-91c6-6ea1b98b6a88',
    'x-rpc-device_name': '',
    'x-rpc-platform': '4',
}

params = {
    'lang': 'zh-cn',
}

json_data = {
    'act_id': 'e202102251931481',
}

response = requests.post(
    'https://sg-hk4e-api.hoyolab.com/event/sol/sign',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# 解析 JSON 数据
data = json.loads(response.text)

# 输出可读内容
#print("Data:", data["data"])
print("签到信息:", data["message"])
#print("Retcode:", data["retcode"])





