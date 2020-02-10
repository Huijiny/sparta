#크롤링 할 기본 상태 준비하기
import requests
from bs4 import BeautifulSoup

#디비 상태 준비하기
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser');
musics = soup.select('.list-wrap > tbody > tr');


for music in musics :
    tag = music.select_one('td > a.title')

    if tag is not None:
        title = tag.text.strip()

        singer = music.select_one(' td > a.artist ').text
        rank = music.select_one('td.number').contents[0].strip()

        doc = {
            'rank' : rank,
            'title' : title,
            'singer' : singer
        }
        print(rank,title,singer)
        db.musics.insert_one(doc)

#뷰티풀 솦 이용해서 크롤링 해오기
#크롤링 된 정보 디비에 저장하기