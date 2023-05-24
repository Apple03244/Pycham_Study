#56.데이터 로드
import pandas as pd
import numpy as np

D=pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv')
d=pd.DataFrame(D)

d.shape

#57.Income_Category의 카테고리를 map 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
dic={'Unknown' : 'N','Less than $40K' : 'a','$40K - $60K' : 'b','$60K - $80K' : 'c','$80K - $120K' : 'd','$120K +' : "e"}
d.columns
'''불필요한 정보를 제거하자'''
d.drop('Unnamed: 0',axis=1,inplace=True)
d['new_columns']=d['Income_Category'].apply(lambda x:dic[x])
d['new_columns'].head(5)

#59.Customer_Age의 값을 이용하여 나이 구간을 AgeState 컬럼으로 정의하라. (0~9 : 0 , 10~19 :10 , 20~29 :20 … 각 구간의 빈도수를 출력하라
d['AgeState']=d['Customer_Age'].apply(lambda x:(x//10)*10)
d['AgeState'].value_counts()

#60.Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼을 정의하고 빈도수를 출력하
d['newEduLevel'] = d['Education_Level'].apply(lambda x: 1 if x.find('Graduate')!=-1 else 0)
d['newEduLevel'].value_counts()

#61.Credit_Limit 컬럼값이 4500 이상인 경우 1 그외의 경우에는 모두 0으로 하는 newLimit 정의하라. newLimit 각 값들의 빈도수를 출력하라
d['newLimit'] = d['Credit_Limit'].apply(lambda x: 1 if x>=4500 else 0)
d['newLimit'].value_counts()

#62.Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라. newState의 각 값들의 빈도수를 출력하라
id1=d['Marital_Status']=='Married'
id2=d['Card_Category']=='Platinum'
d['newstate']=d[['Marital_Status','Card_Category']].apply(lambda x:1 if x=='Married' & x=='Platinum' else 0)

