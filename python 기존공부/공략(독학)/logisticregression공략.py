#LogisticRegression
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

#데이터 불러오기
D=pd.read_csv('C:/Users/SAMSUNG/파이썬 스터디/Personal_Loan.csv')
data=pd.DataFrame(D)

#데이터 확인하기
data.info()
data.describe()
data.head(2)

#전처리
data.drop(['ID','ZIP Code'],axis=1,inplace=True)

#타켓변수,목적변수 설정
target=data['Personal Loan']
feature=data[data.columns.difference(['Personal Loan'])]

#train,test setting
from sklearn.model_selection import train_test_split
trainx,testx,trainy,testy=train_test_split(feature,target,train_size=0.7,random_state=10)









from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn import metrics
