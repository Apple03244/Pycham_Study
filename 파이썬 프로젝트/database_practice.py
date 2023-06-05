import requests
import json
#pip install json
url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)
data_json = json.loads(response.text)
print(data_json[0])
# 출력 결과
# "symbol" : "BTCUSDT", "lastPrice" : xxxxx(가격)
for a in data_json:
    if a['symbol'] == "BTCUSDT":
        # print(f"{a['symbol']}코인의 price는 {a['lastPrice']} 입니다.")


import pymysql as py
import time
import requests
import json

while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data_json = json.loads(response.text)
    time.sleep(10)
    for x in data_json:
        if x["symbol"]=="BTCUSDT":
            try:
                connector = py.connect(host="localhost", port=3306, user="root", password="1234",
                                       database="my_practice")
                cursor = connector.cursor()
                add_data = "INSERT INTO  practice(coin_name, last_price) VALUES(%s,%s)"
                data=(x['symbol'],x['lastPrice'])
                cursor.execute(add_data, data)
                connector.commit()
                cursor.close()
                connector.close()

            except py.connect.Error as err:
                print("error")

