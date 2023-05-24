import numpy as np
#array : 행렬 만들기 [[]]
data=np.array([[1,2,3],[3,4,5]])
data_0=np.zeros([2,3])
data_1=np.ones([1,4])

#브로드캐스팅
idx=data>=4
data[idx]=100
data

#모양바꾸기
data.reshape([1,6])

#타입 변환
data.astype("str")
data

