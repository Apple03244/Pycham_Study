# while True:
#     try:
#         n1=int(input("num1: "))
#         n2=int(input("num2: "))
#         print(n1/n2)
#
#     except ZeroDivisionError as zd:
#         print(f'{zd} 오류입니다')
#     except Exception:
#         print(f"{Exception}오류입니다")
#     finally:
#         print("결과를 확인해주세요")
#

#에러강제의 예시
while True:
    raise Exception

class Bird:
    def fly(self):
        raise Exception

class Eagle(Bird):
    def fly(self):
        print("Fly")


Eagle1=Eagle()
Eagle1.fly()

#오버라이딩 하라고~ 부모클라스에 예외를 강제함

