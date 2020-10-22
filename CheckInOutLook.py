import requests
import os


# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer})
    state = requests.get(url2, headers={'cookie': cookie, 'referer': referer})
    print(state.json())

    # if 'message' in checkin.text:
    #     mess = checkin.json()['message']
    #     time = state.json()['data']['leftDays']
    #     time = time.split('.')[0]
    #     print('OUTLOOK剩余' + time + '天')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
