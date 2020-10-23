import requests
import os


# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]

header = {
    'Host': 'glados.rocks',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json;charset=utf-8',
    'Content-Length': '26',
    'Origin': 'https://glados.rocks',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://glados.rocks/console/checkin',
    'Cookie': cookie,
}

data = '{"token":"glados_network"}'

def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url, headers=header,data=data)
    state = requests.get(url2, headers=header,data=data)
    print(checkin.content.decode("utf-8"))

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print('EDU剩余' + time + '天')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
