# import json
import requests
import json
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_sslify import SSLify

# TODO: 突破 IP 訪問限制
# TODO: 避免 client 有大量可疑請求(同IP)
# TODO: 每 x 毫秒就重新 call 一次 API，假設 FTX 因限制不能 call 就換幣安等多個交易所

app = Flask(__name__)
CORS(app)

@app.route('/getData', methods=['GET'])
def getTable():
    
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
