## 2025.09.30 과제
## 이서범

## --------------------------------------------------
## 1. 재귀호출로 회문 판별하기

## 설계도
## 1. 회문 -> 첫 단어와 끝 단어가 한칸씩 줄며 비교하였을 때, 동일한 형태의 단어
## 2. 재귀호출의 형태 -> 반복적으로 줄어서 호출될때 이전 호출과 다른 형태의 단어가 되어야함
## 3. 판별 -> 첫 단어와 끝 단어가 같으면 True
##        -> 만약 단어 확인 폭이 줄었을 때, 한 번이라도 첫 단어와 끝 단어가 같지 않으면 False


print("#1.")
def is_palindrome(word):
    if len(word) < 2: ## 여기까지 줄어들었다는건, 중간에 False가 없었다는 것
        return True
        
    if word[0] is not word[-1] :
        return False
    
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))
print(is_palindrome('helleh'))


# ## --------------------------------------------------
## 2. 피보나치 수열을 재귀함수로 설계
print("#2.")
def fib(n):
    if n <= 1: ## 여기까지는 자기 자신이 더한 값이니깐 그대로 n으로 출력하기
        return n
    return fib(n-1) + fib(n-2)

n = int(input('피보나치 원하는 숫자 입력 : '))
print(fib(n))


## --------------------------------------------------
## 3. 호출 횟수를 세는 함수 만들기 (클로저 사용)
print("#3.")
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i

    return count

c = counter()
for i in range(10):
    print(c(), end=' ')


## --------------------------------------------------
## 4. 카운트다운 함수 만들기 (클로저 사용)
print("\n#4.")
def countdown(n):
    n += 1
    def count():
        nonlocal n
        n -= 1
        return n
    return count

n = int(input('원하는 카운트다운 숫자 입력 : '))
c = countdown(n)

for i in range(n):
    print(c(),end=' ')


