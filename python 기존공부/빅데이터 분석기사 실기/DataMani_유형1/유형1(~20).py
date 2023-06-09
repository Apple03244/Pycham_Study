import datetime

import pandas as pd
import numpy as np
D=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv')
D2=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv')

data1=pd.DataFrame(D) #비디오 정보
data2=pd.DataFrame(D2) #참가자 채널 정보

data1.ct
data2.ct

help(pd.to_datetime)
#11.각 데이터의 ‘ct’컬럼을 시간으로 인식할수 있게 datatype을 변경하고 video 데이터의 videoname의 각 value 마다 몇개의 데이터씩 가지고 있는지 확인하라
def daychange(x):
    return pd.to_datetime(x,format='%Y-%m-%d %H:%M:%S')

data1["ct"]=data1["ct"].apply(daychange)
data2['ct']=data2['ct'].apply(daychange)

answer=pd.DataFrame(data1.groupby(['videoname'])['ct'].count())

#12.수집된 각 video의 가장 최신화 된 날짜의 viewcount값을 출력하라
data1['viewcount_temp']=data1.groupby(['videoname'])['ct'].transform(np.count_nonzero)
data1["answer"]=data1.groupby('videoname')['ct'].transform(np.max)
data1[["viewcount_temp",'videoname','answer']]

#13.Channel 데이터중 2021-10-03일 이후 각 채널의 처음 기록 됐던 구독자 수(subcnt)를 출력하라
test=data2[data2['ct']>='2021-10-03']
test.groupby(['channelname'])[['ct','subcnt']].min()

#14.각채널의 2021-10-03 03:00:00 ~ 2021-11-01 15:00:00 까지 구독자수 (subcnt) 의 증가량을 구하여라
test1=data2.loc[data2.ct>='2021-10-03 03:00:00']
test2=data2.loc[data2.ct<='2021-11-01 15:00:00']
result=pd.merge(test1,test2,how='inner')
result=result.groupby(["channelname"])['subcnt'].apply(np.diff)
pd.DataFrame(map(sum,result),result.index)

import datetime
#15.각 비디오는 10분 간격으로 구독자수, 좋아요, 싫어요수, 댓글수가 수집된것으로 알려졌다. 공범 EP1의 비디오정보 데이터중 수집간격이 5분 이하, 20분이상인 데이터 구간( 해당 시점 전,후) 의 시각을 모두 출력하라
pre_data=data1.loc[data1['videoname']==' 공범 EP1']
pre_data=pre_data.sort_values("ct").reset_index(drop=True)
temp=pre_data.loc[(pre_data.ct.diff(1)>=datetime.timedelta(minutes=20))|(pre_data.ct.diff(1)<=datetime.timedelta(minutes=5))].index
result=[]
for x in temp:
    result.append(x)
    result.append(x-1)
    result.append(x+1)
res