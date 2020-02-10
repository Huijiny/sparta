from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.
app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.


@app.route('/')
def home():
    return render_template('memo.html')

@app.route('/post', methods=['GET'])
def listing():
    articles = list(db.articles.find({},{'_id': False}))
    return jsonify({'result' : 'success', 'articles': articles})

@app.route('/post', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    image_url = og_image['content']
    title_url = og_title['content']
    descrip_url = og_description['content']

    article = {'url': url_receive, 'comment': comment_receive, 'image': image_url,
               'title': title_url, 'desc': descrip_url}

    db.articles.insert_one(article)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)