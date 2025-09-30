## -------------------------------------------------------------
## 재귀함수(Recursive Function)
## - 함수 내부에서 자기 자신을 다시 호출하는 함수
## - 알고리즘 구현에 많이 사용됨
## - 대표적인 예: 피보나치 수열, 팩토리얼 
## -------------------------------------------------------------
## 함수기능 : 팩토리얼(Factorial) 결과 반환 함수 구현
## 함수이름 : nomalFactorial
## 매개변수 : num   - int 정수
## 결과반환 : 팩토리얼 결과 반환
## -------------------------------------------------------------
# def nomalFactorial(num):
#     total = 1
#     for n in range(num,0,-1):
#         total = total * n
#     print(f'{num}! = {total}')
#     return total

# ## 함수사용 
# nomalFactorial(5)
# nomalFactorial(9)


## -------------------------------------------------------------
## 함수기능 : 재귀호출기반의 팩토리얼(Factorial) 결과 반환 함수 구현
## 함수이름 : recFactorial
## 매개변수 : num   - int 정수
## 결과반환 : 팩토리얼 결과 반환
## -------------------------------------------------------------
def recFactorial(num):
    ## 종료조건
    if num == 1:
        return 1
    
    return num * recFactorial(num-1)


## 함수사용 
recFactorial(5)
recFactorial(9)
