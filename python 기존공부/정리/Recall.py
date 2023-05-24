#Pandas,Series
import numpy as np
import pandas as pd
s1=pd.Series([1,2,3]) # 0 베이스
s2=pd.Series(["a","b","c"],[1,2,3]) #뒤가 인덱스였구낭
s3=pd.Series(np.arange(200))
s4=pd.Series(np.arange(100),np.arange(101,201),dtype=np.int16)
s7=pd.Series(np.arange(100),s4) #value를 인덱스로~
s4,s7
s8=pd.Series(np.arange(100),s4.index) #value를 인덱스로~

#Series를 왜 함?
#DataFrame=2차원 Series

#Series를 DataFrame으로 recall
D=pd.read_csv("C:/Users/SAMSUNG/Desktop/빅데이터 분석기사/games.csv")
data=pd.DataFrame(D)
data.info()
s1=data["t1_champ1id"] #데이터 플레임 한줄
s1.index
s1.count() #그냥 셈
s1.value_counts() #빈도를 나타내줌
s1.unique() #이게 뭘 의미하는지는
idx=s1==8
s1[idx]
s1[idx].count()
idx2=s1>=s1.mean()
s1[idx2].index

#위의 방법
#Boolean selection

#loc : 자체, ilic : 0base
A=dict(zip(['a','b','c'],range(3)))
B=pd.DataFrame(A,['x','y','z'])
B
B[['a','b','c']]=[[1,2,3],[4,5,6],[7,8,9]]
B.iloc[1]
B.loc["y"]

B[['a','b']]

# dataframe
data.columns
data=data[['gameId','t1_champ1id','t1_ban1']]
data['gameId'].value_counts()
data['t1_ban1'].value_counts()
data['t1_ban1'].count()
data['t1_ban1'].sum()
data.drop(['t1_ban1'],axis=1)
data

#시각화
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.__version__

df = sns.load_dataset('penguins')
sns.pairplot(df, hue='species')

sns.pairplot(data.corr())

%matplotlib inline
data.corr()
plt.matshow(data.corr())