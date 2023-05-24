#8,8 무작위 행렬
import random as rd
import numpy as np

data=np.random.randint(100,300,size=(8,8)) #np.random 이 기본으로 지급되나봄
data

#브로드캐스팅

idx1=data%3==0
idx2=data%5==0
idx3=data%15==0

#타입 변환
array=data.astype("str")
array
#값 변환
array[idx1]="3의 배수"
array[idx2]="5의 배수"
array[idx3]="15의 배수"

#확인
'''원래 안되는 거였네'''
