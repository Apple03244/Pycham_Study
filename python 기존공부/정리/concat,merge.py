'''
concat: normarly sum for two data frames
merge : sum of two data frames about some tempt(index)
'''
import pandas as pd
import numpy as np

#cancat & merge
D=pd.read_csv('C:/Users/SAMSUNG/Desktop/빅데이터 분석기사/타이타닉/train.csv')
D.columns
data1=pd.DataFrame(D)
data1.drop(['Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],axis=1,inplace=True)
data1
data2=pd.DataFrame(D)
data2.drop(['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp'],axis=1,inplace=True)
data2

data1.head(2), data2.head(2)
#concat
test1=data1.iloc[:2]
test2=data1.iloc[2:5]

test=pd.concat([test1,test2],axis=1)
test=pd.concat([test1,test2],axis=0,join='inner',ignore_index=True)

test=pd.concat([test1,test2],axis=1,ignore_index=False)

#merge
test=pd.merge(test1,test2,how='right',on="PassengerId")
test


customer=pd.DataFrame({"customer_Id":np.arange(6),"name":["A","B","C","D","E","F"],"age":[40,20,21,30,35,19]})

oders=pd.DataFrame({"customer_Id":[1,1,2,2,2,3,3,1,4,9],
                    "item":["치약","칫솔","생수","이어폰","수건","면도기","스티커","케이스","아령","음료수"]
                   ,"quantity":[1,2,1,1,3,2,2,3,2,1]})

prt1=pd.concat([customer,oders],ignore_index=True)
prt1

#concat : 단순 합치기

prt1=pd.merge(customer,oders,how='left',on='customer_Id')
prt2=pd.merge(customer,oders,how='inner',on='customer_Id')
prt3=pd.merge(customer,oders,how='right',on='customer_Id')
prt2

#없으면 drop 되어버리네..?

ct=customer.set_index('customer_Id')
od=oders.set_index('customer_Id')

ct,od

df=pd.merge(ct,od,left_index=True,right_index=True)
df.sort_values("quantity",ascending=False)

df=pd.merge(customer,oders,on='customer_Id',how='inner').groupby('item').sum()

pd.merge(customer,oders,on='customer_Id',how='inner').groupby(['name','item']).sum().loc['C']