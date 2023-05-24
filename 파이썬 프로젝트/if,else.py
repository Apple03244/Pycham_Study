score=int(input("점수를 입력하세요~: "))
if score>=70:
    print("합격입니다")
else:
    print("불합격입니다")

#1_problem
a=int(input("자연수를 입력하세요"))
if a%2==1:
    print("홀수")
else:
    print("짝수")


#2_problem
a=int(input("점수를 입력하세요"))
b=int(input("점수를 입력하세요"))
c=int(input("점수를 입력하세요"))

if a+b+c>=240:
    print("합격입니다")
else:
    print("불합격입니다")


a=int((input("정수를 입력하세요: ")))
b=int((input("정수를 입력하세요: ")))

print("두 수의 합은 :",a+b)
if a-b<0:
    x=b-a
else:
    x=a-b
print("두 수의 차는 :",x)

import sys
print(sys.version)

a,b=int(input("나이를 입력하세요: " )),float(input("키를 입력하세요: "))
result=["키가 큽니다","키가 보통입니다"]
if a>=40:
    if b>=175:
        print(result[0])
    else:
        print(result[1])
else:
    if b>=180:
        print(result[0])
    else:
        print(result[1])

a,b,c=int(input()),int(input()),int(input())
print(max([a,b,c]))
'''
if a>=b:
else

귀찮...
'''

