# import json
import requests
import json
import time
from investiny import historical_data, search_assets
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_sslify import SSLify
from datetime import datetime, timedelta

# TODO: 突破 IP 訪問限制
# TODO: 避免 client 有大量可疑請求(同IP)
# TODO: 每 x 毫秒就重新 call 一次 API，假設 FTX 因限制不能 call 就換幣安等多個交易所

app = Flask(__name__)
CORS(app)

@app.route('/getBlockHeight', methods=['GET'])
def getBlockHeight():
    # get block hash
    hashURL = 'https://chain.api.btc.com/v3/block/latest/tx?verbose=2'
    hashTxt = requests.get(hashURL).text
    data = json.loads(hashTxt)
    block_hash = data['data']['list'][0]['block_hash']

    # get block height
    heightUrl = 'https://blockchain.info/rawblock/' + block_hash
    heightTxt = requests.get(heightUrl).text
    data = json.loads(heightTxt)
    return str(data['height'])

@app.route('/getData', methods=['GET'])
def getData():
    
    coin = request.args.get('coin')
    if coin == None:
        return 'Error: 請給我交易對'

    elif '/' not in coin:
        return 'Error: 交易對格式錯誤'

    else:
        url = 'https://ftx.com/api/markets/' + coin # ex: BTC/USDT
        txt = requests.get(url).text
        data = json.loads(txt)
        
        return data

@app.route('/getStock', methods=['GET'])
def getStock():
    nameList = [
        'BTC-PERP', 'ETH-PERP',
        'BTC/USD', 'ETH/USD',
        'APT-PERP', 'SOL-PERP',
        'XRP-PERP', 'MATIC-PERP',
        'ATOM-PERP', 'APT/USD'
    ]
    dataList = []
    
    # get data from FTX
    # {name: 'name', price: price, gain: gain}
    # str, float, float
    for name in nameList:
        url = "https://ftx.com/api/markets/" + name
        txt = requests.get(url).text
        data = json.loads(txt)

        tmp = {
            "name": data['result']['name'],
            "price": data['result']['price'],
            "gain": round(float(data['result']['change24h']) * 100, 2)
        }
        
        dataList.append(tmp)
    return dataList

@app.route('/getStockGain', methods=['GET'])
def getStockGain():

    query = request.args.get('query')
    type = request.args.get('type')
    exchange = request.args.get('exchange')
    if query == None or type == None or exchange == None:
        return 'Error: 請給我正確的參數: query + type + exchange'
        
    else:
        # get current price
        results = search_assets(query = query, limit = 1, type = type, exchange = exchange)
        
        # get investing id
        investing_id = int(results[0]["ticker"])
        
        # get historical data
        data = historical_data(investing_id = investing_id)
        return str(round((data['close'][-1] - data['close'][-2]) / data['close'][-2]*100, 2)) + "%"

@app.route('/', methods=['GET'])
def root():
    return '''
    <h1>歡迎來到API</h1>
    <p>可以使用 /getData 來得到資訊</p>
    '''
    
# @app.route('/test_api2/', methods=['GET'])
# def test_api2():
#     return json.dumps(message='Hello, API2')

if __name__ == '__main__':

    # You should not put your ssl cert file be
#    app.run(host='0.0.0.0', port=8080, debug=False, ssl_context=('certificate.pem', 'private.pem'))
    app.run(host='0.0.0.0', port=8080, debug=False)
