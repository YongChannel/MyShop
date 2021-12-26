from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# import requests
# from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']


    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive, headers=headers)
    #
    # soup = BeautifulSoup(data.text, 'html.parser')
    #
    # title = soup.select_one('meta[property="og:title"]')['content']
    # image = soup.select_one('meta[property="og:image"]')['content']
    # desc= soup.select_one('meta[property="og:description"]')['content']


    doc = {'name': name_receive, 'quantity': quantity_receive, 'address': address_receive, 'phone': phone_receive}
    db.order.insert_one(doc)
    return jsonify({'msg':'"댕댕이: 주문완료!"'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.order.find({}, {'_id':False}))
    return jsonify({'all_order_txt':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)