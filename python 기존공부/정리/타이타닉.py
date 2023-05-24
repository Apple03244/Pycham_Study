#1.Seaborn
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

#기본
import pandas as pd
import numpy as np

#데이터 프레임부터 만들어볼까
D=pd.read_csv('C:/Users/SAMSUNG/Desktop/빅데이터 분석기사/타이타닉/train.csv')
data=pd.DataFrame(D)

#데이터 확인
data.info()
data.describe()

#열이 너무 많음..
data.columns

#인덱스를 passengerid로 바꾸기
data.set_index(keys=['PassengerId'],drop=True,inplace=True)
data

#불필요 column 삭제
data.columns
data.drop(data.columns.difference(['Survived','Pclass','Sex','Age']),axis=1,inplace=True) #inplace 설정 확인하기
data

#행 확인
data[['Survived','Sex']]
data.iloc[2] #이건 제로 베이스이니까
data.loc[3]

#남자면서 생존
S=data['Survived']==1
M=data['Sex']=='male'
data[S&M]

#corr : 연속형 데이터에만 적용
data.info

#Nan 값 찾기
data.info() #age에 891-714개의 Nan 확인
data.isna()

#Nan값 처리
data.dropna(subset=['Age'],inplace=False) #any,all 설정이 되네?

data['Age'].fillna(data['Age'].mean(),inplace=True)

data[data['Age']==data['Age'].mean()]

#bin
import math
def cutf(x):
    if math.isnan(x):
        return 0
    return math.floor(x/10)*10

data['Age'].apply(cutf)

#꼭 apply 함수를 사용해야하나..?
data['Age_category']=list(map(cutf,data['Age']))

#map을 이용할 수 있었다~

#one hot encoding : 벡터 부여---자연어 처리가 예시
data1=pd.get_dummies(data,columns=['Sex'],drop_first=False)
data1[['Sex_male','Sex_female']].astype(int)

#groupby
group=data.groupby(["Sex",'Pclass'])
group.groups
group.mean()

