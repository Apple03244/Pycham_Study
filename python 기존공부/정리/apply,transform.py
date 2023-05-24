import pandas as pd
import numpy as np
import random as rd


D=pd.read_csv('C:/Users/SAMSUNG/Desktop/빅데이터 분석기사/타이타닉/train.csv')
data=pd.DataFrame(D)

data.set_index(['PassengerId'],drop=True,inplace=True)
data.drop(data.columns.difference(['Survived','Pclass','Sex','Age']),axis=1,inplace=True)
data

#transform 과 apply 차이?

test=pd.DataFrame(np.random.randint(1,10,size=(3,3)),['a','b','c'],['x','y','z'])
test.x #오 이게 되네..?

test['r_sum']=test.apply(lambda x:x.x+x.y+x.z,axis=1)
test.drop("sum",axis=1,inplace=True)
test
test.append()