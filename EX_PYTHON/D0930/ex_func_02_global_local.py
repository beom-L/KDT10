
## 전역 변수 선언
year = 2025
loc = '대구'

## 사용자 정의 함수
## 지역 변수명과 전역 변수명 동일할 경우
## -> 함수에서는 지역변수 사용함 !
def showInfo():
    year = 2030
    print(f'올해년도 : {year}')
    print(f'우리지역 : {loc}')   ## 1. 함수안에서 찾기  <= 읽기만 하는거임
                                ## 2. 함수 밖에서 찾기 <- 밖에도 없으면 ERROR 발생

def changeInfo():
    global year               ## 명시적으로 전역변수를 사용하겠다고 설정
    year = year + 1           ## 전역변수 year        <= 값 변경할려고 함
    print(f'올해 년도 : {year}')
    print(f'우리 지역 : {loc}') ## 전역변수 loc


## 기능구현
showInfo()
changeInfo()
print(year) ## <= 전역변수 year 사용