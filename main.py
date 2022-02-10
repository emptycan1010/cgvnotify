from bs4 import BeautifulSoup
import requests
import time
i = 0
o = 0
while i <= 0:
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0128&date=20220301&screencodes=&screenratingcode=&regioncode='
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a> strong').text.strip()
        date = soup.select_one('#slider > div > ul').text.strip()
        # print (date)
        val = date.find("01")
        if(val == -1):
            print("attempted" + str(o))
            o += 1
            time.sleep(1)
        else:
            if("배트맨" in title):
                print(title + ' IMAX 예매 확인')
                i = 1
            else:
                print("attempted" + str(o))
                o += 1
                time.sleep(1)
