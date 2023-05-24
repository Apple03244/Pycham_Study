for x in range(101):
    if not x%3 and  not x%5:
        print(x)

for x in range(101):
    if not x%5 and x%10:
        print(x,end='\t')


x,y=int(input("시작숫자: ")),int(input("종료숫자: "))
result=0
for i in range(x,y+1):
    if not i%4:
        result+=i
print(result)

#팩토리얼

n=int(input("숫자: "))
result=1
for x in range(n,0,-1):
    result*=x
    print(x,end="X")
print("1")
print("결과:",result)

print("구구단")
for i in range(2,10):
    print(f'{i}단')
    for j in range(1,10):
        print(f'{i}x{j}={i*j}',end='\n')
    print('',end="\t")

print("구구단 pycham")
for i in range(2,10):
    print(f'{i}단: ',end="")
    for j in range(1,10):
        print(f'{i*j}',end='\t')
    print()


for num2 in range(1,10):
    for num1 in range(2,10):
        print("{}*{}={}".format(num1,num2,num1*num2),end="\t")
    print()

for x in range(5):
    print('*'*(x+1))

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(6):
    print(" "*(5-i),"*"*i)

i=1
while i<11:
    print(i)
    i+=2

i=int(input('자연수를 입력하세요: '))
while i>0:
    print(i,"!")
    i-=1

result=0
while True:
    i=int(input("0을 입력하면 멈춤니다: "))
    if not i:
        break
    result+=i
print(result)

sentence=""
while True:
    x=str(input("문자를 입력하세요(종료는 . 입니다): "))
    if x=='.':
        break
    sentence+=x
print(sentence.count("a"),sentence)


result=0
while True:
    x=str(input("문자 입력: "))
    if x=="a":
        result+=1
    elif x==".":
        break
print(result)

while 1:
    x=int(input())
    if x==-1:
        print("실행종료")
        break
    for y in range(x):
        print("*",end="")
    print()


import random

while 1:
    x = random.randint(1,10)
    if x==3:
        print("실행종료")
        break
    print("*"*x)

#1.
ls=["Banana",'Apple','Orange']
ls.append("Tomato")
ls.remove("Apple")
ls

#2.
tup=(-10,0,10,20,30,40,50,60)
tup[2:6]
len(tup)
tup.index(60)+1

#3.
dic=dict(zip(['성인','청소년','아동'],[8000,5000,5000]))
dic

dic['어린이']=3000
dic.pop('아동')
dic

#4.
n=int(input('동물 수: '))
result=[]
for i in range(n):
    result.append(input('이름: '))
print(result)

#5
for x in dic:
    print(f'<{x}입장료 - {dic[x]}>')

#6
ls=[20,55,10,3,85,36,70,64]

result={"최댓값":20,"최솟값":20,"평균":0}
for x in ls:
    if x>=result['최댓값']:
        result['최댓값']=x
    if x<=result["최솟값"]:
        result["최솟값"]=x
    result["평균"]+=x
result["평균"]/=len(ls)
for x,y in result.items():
    print(f'{x} : {y}')


def f():
    print("월요일입니다."*5)
f()

def f(x,y):
    for i in range(y):
        print(x)

f('안녕',5)

def f(x,y,i,j):
    return (x+y+i+j)/4

f(1,2,3,4)

def message():
    n=int(input("출력할 횟수 입력: "))
    for i in range(n):
        print("Time waits for no one")
message()

def f():
    n=int(input("정수1 입력: "))
    m=int(input("정수2 입력: "))
    print(''' 
    ---------------
    두 수의 연산 선택
    ---------------
    1. 합
    2. 차
    3. 곱
    4. 나눗셈
    ---------------''')
    ls=[n,m]
    dic={1:n+m,2:max(ls)-min(ls),3:n*m,4:max(ls)/min(ls)}
    oder=int(input("연산을 선택하시오: "))
    print("연산결과: ",dic[oder])
f()