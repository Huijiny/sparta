import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')
booked_tickets = soup.select('#reserveRanking0 > ul > li')

for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    a_points = movie.select_one('td.point')
    if a_tag is not None:
        ## a의 text를 찍어본다.
        print (a_tag.text , a_points.text)

for booked_ticket in booked_tickets :
   name = booked_ticket.select_one(' a ')
   stars = booked_ticket.select_one('span.ratio')
   if name is not None:
      print(name['title'], stars.text)
