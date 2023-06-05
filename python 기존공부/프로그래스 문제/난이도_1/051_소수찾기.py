# def solution(n):
#     prime = lambda x: 1 if all([bool(x % i) for i in range(2, x)]) else 0
#     result=0
#     if n==2:
#         return 1
#     elif n==1:
#         return 0
#     else:
#         for num in range(3,n+1):
#             result+=prime(num)
#         return result+1 #2를 계산하지 않았기 때문

#효율성이 안나옴
def solution(x):
    if x==1:
        result=[]
    elif x==2:
        return [2]
    else:
        test = list(range(1,x+1))
        i=2
        while True:
           for y in test:
               if y%i==0 and y//i!=0:
                   test.remove(y)
                    pass
            return test

solution(10)


