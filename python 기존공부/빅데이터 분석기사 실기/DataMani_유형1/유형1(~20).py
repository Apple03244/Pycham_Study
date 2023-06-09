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
test=data2.loc[data2["ct"]>pd.to_datetime('2021-10-03')].groupby('channelname')['ct'].min()
pd.merge(data2,test,how="inner")[['channelname','subcnt']]