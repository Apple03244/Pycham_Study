#클래스!!!
'''
1. 같은 기능의 함수 집함
2. 객체를 만들기 위해
'''
#명명 규칙 : 일반적으로 대문자 알파벳으로 시작
#변수명 함수명은 소문자로 시작 -> camalcase #예로 myList,myImportantList
# class Calculator:
#     result=0
#     def plus(a):
#         Calculator.result+=a
#     def minus(a):
#         Calculator.result-=a
#     def multiply(a):
#         Calculator.result*=a
#     def divide(a):
#         Calculator.result/=a

Calculator.plus(10,20)
Calculator.plus(10)
Calculator.result

class Calculator:
    result=0
    @classmethod #클래스 내에서 선언된 함수는 매서드라고 부른다
    def plus(cls,a):
        cls.result+=a #cls 자리에 Calculator 이 들어옴
    def minus(cls,a):
        cls.result-=a
    def multiply(a):
        cls.result*=a
    def divide(a):
        cls.result/=a

#객체의 사용이유
#클래스의 중복제거 : 변수와 함수의 재활용에 어려움 해결?
#객체 형식의 클래스 작성

class Calculator:
    #객체가 생성될때 init은 가장 먼저 실행
    def __init__(self):
        self.result=0
    def plus(self,a):
        self.result+=a #cls 자리에 Calculator 이 들어옴
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a
    def divide(self,a):
        self.result/=a

A=Calculator()
B=Calculator()

A.plus(100)
A.result

#초기값 받기
class Calculator:
    #객체가 생성될때 init은 가장 먼저 실행
    def __init__(self,result):
        self.result=result
    def plus(self,a):
        self.result+=a #cls 자리에 Calculator 이 들어옴
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a
    def divide(self,a):
        self.result/=a

A=Calculator(100)
A.result

from datetime import datetime

#실습
class Person:
    def __init__(self,name,age,gender,email):
        self.name=name
        self.age=age
        self.gendef=gender
        self.email=email

    def register(self):
        self.myInfo=self.name+" "+str(self.age)+" "+self.gendef+" "+self.email+" "+str(datetime.now())

P1=Person('이정훈',28,"남자","apple03244@gmail.com")
P1.register()
P1.myInfo

dic={1:100,2:200}
dic.1
P2=Person("김모모",25,"여자",'apple03244@kakao.com')
P2.register()
P2.myInfo

id(Person)

#클래스의 상속 : 부모클래스에서의 기능을 자식 클래스에서 물려받는 것.
#class 자식 클래스명(부모클래스명) 이런 형식으로 선언
class Calculator:
    #객체가 생성될때 init은 가장 먼저 실행
    def __init__(self,result):
        self.result=result
    def plus(self,a):
        self.result+=a #cls 자리에 Calculator 이 들어옴
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a
    def divide(self,a):
        self.result/=a
    # @overload : 파이썬에선 오버로딩을 지원하지않음.
    #
    # def divide(self,a,b):
    #     self.result/=(a+b)
    #     #이건 오버로딩 : overloading

class CalculatorBaby(Calculator):
    pass
#만약 부모에게 있는 기능을 자식클래스에서 다시 정의하면
#overriding : 덮어써진다

k=CalculatorBaby(10)
k.divide(5)
k.result

k2=CalculatorBaby(10)
k2.divide(5.2)
k2.result

CalculatorBaby
help(print)
dir(print)

if __name__=="__main__": 이걸 넣으면 import 해와도 실행안됌
