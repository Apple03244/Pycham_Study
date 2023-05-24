# matplot 완전이해
import numpy as np
import matplotlib.pyplot as plt

x, y = np.random.randint(1, 10, 3), np.random.randint(1, 10, 3)
x, y
x=np.array([2,4,8])
'''
x=2,4,8
y=7,5,9
'''

# plot은 선을 기본으로 제공
plt.plot(x)  # 단일 입력시 y값으로 인지, x축은 자동으로 만듬
plt.show()

plt.plot(x, y) #순서 쉽죠? x축, y축 순입니다
plt.show()

#plt 꾸미기(문자형, x,y의 최대.최소 바꾸기

plt.plot(x,y,"r-")
plt.axis([0,10,0,20]) #x부터y
plt.show()

#한꺼번에 여러개의 그래프--내부 모양을 자동으로 array로 인식,formating이 잘되네
i=np.arange(0,10)
plt.plot(i,i,'r-',i,i**2,'bo',i,i**3,'y^')
plt.show()

#dict상테의 matplt
dic_data={'x':x,"y":y}
dic_data

plt.plot('x','y',data=dic_data)

#Label
plt.plot('x','y',data=dic_data)
plt.xlabel("x",labelpad=10,loc="left") #거리 조절이구만
plt.ylabel("y",loc='top')

#다중 그래프:하나의 창에 열기
plt.subplot(121)
plt.plot('x','x',data=dic_data)

plt.subplot(122)
plt.plot('x','y',data=dic_data)

plt.show()

#똑같은 상황이지만 각각 창을 부여하고 싶다면?
plt.figure(1)
plt.plot('x','x',data=dic_data)

plt.figure(2)
plt.plot('x','y',data=dic_data)