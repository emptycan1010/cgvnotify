from bs4 import BeautifulSoup
import requests
import telegram
import aiohttp
import time

i = 0
o = 0

chat_token = "your_token_here"
tel = telegram.Bot(token = chat_token)
while i <= 0:
    # title_list = soup.select('div.info-movie')
    # for i in title_list:
    #     i.select_one('a > strong').text.strip()
# 실 사용시 theatercode와 date를 수정해서 사용해주세요
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0005&date=20211225&screencodes=&screenratingcode=&regioncode='
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
        val = date.find("25") # 25일의 예매창 존재여부를 확인합니다. 다음페이지로 넘어가있을시 작동하지 않을 확률이 큽니다. 
                              # 링크로 바로 해당일 예매 존재여부를 확인할수있다면 비활성화해도 좋습니다.
        if(val == -1):
            print(o)
            o = o+1
            time.sleep(1) # 해당하는 날이 없을시 1초를 쉽니다. 더 빠른 반응을 위해서라면 해당 줄을 주석처리해주세요.
        else:
            if(title == '스파이더맨-노 웨이 홈'):
                print(title + ' IMAX 예매가 열렸습니다.')
                tel.send_message(chat_id=your_chat_id_here, text= title + ' 예매 오픈!')
                i = 1
