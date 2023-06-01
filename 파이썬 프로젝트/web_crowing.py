import requests

# https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8
header={"User-Agent" : "Mozilla/5.0"}
response=requests.get(url, headers=header)
html_response=BeautifulSoup(response.test,'html.parser')

#원하는 정보 추출
#감독정보 제작비 정보

director_info=html_response.select_one("table.infobox > tbody > tr:nth-of-type(3) > td").get_txt()
budget_info=html_response.select_one("table.infobox > tbody > tr:nth-of-type(8)")

'''
('table.infobox
'''

#코인 시세정보 API : JSOON 데이터 많이 쓰임
url = "https://api.binance.com/api/v3/ticker/24hr"
import json
response=requests.get(url)
data_json=json.loads(response.text)
print(data_json)
result=[]
for a in data_json:
    if a['symbol']=='BTCUSDT':
        result.append([a['symbol'],a['lastPrice']])
print(result)

# csv 파일 파싱