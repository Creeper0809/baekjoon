import requests
from bs4 import BeautifulSoup
import time


def crawl():
    url = 'http://aivojs.cju.ac.kr/status.php?&problem_id=1061&jresult=4'
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            count = soup.select_one('#result-tab > tbody')
            print("-"*30)
            for i in range(1, len(count)):
                title = soup.select_one('#result-tab > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(8)')
                if title is None:
                    break
                print(int(title.getText().split(" ")[0]))
                if 209 > int(title.getText().split(" ")[0]):
                    print("경고!!")
                    return
        else:
            print(response.status_code)
        time.sleep(600)


crawl()
