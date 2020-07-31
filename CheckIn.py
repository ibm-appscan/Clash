import requests


# 填入glados账号对应cookie
cookie = "__cfduid=da59bde2fcc0d167abbf144e9efd199341596083188; _ga=GA1.2.1897939625.1596083194; _gid=GA1.2.1022595244.1596083194; koa:sess=eyJ1c2VySWQiOjQ1NjIxLCJfZXhwaXJlIjoxNjIyMDEzNDM3MDA3LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=ZESXtj5KPiX5rAmZc-3R0dAphEE"


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer})
    state = requests.get(url2, headers={'cookie': cookie, 'referer': referer})

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(mess)
        print('剩余' + time + '天')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
