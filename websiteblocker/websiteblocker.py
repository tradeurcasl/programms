import time
from datetime import datetime as dt

temp_path_to_hosts = r'C:\Users\loftyrogue\hosts' #anyplace you want to place ur local test-copy of hosts-file
path_to_hosts = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['www.yandex.ru',
                'yandex.ru',
                '*.yandex.*']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working process')
        with open(path_to_hosts, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(path_to_hosts, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('You are free... For now')

    time.sleep(10)