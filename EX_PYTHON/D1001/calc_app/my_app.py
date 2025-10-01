## --------------------------------------------------------
## 계산기 프로그램
## - 4칙 연산
## - 연산 결과/이력 저장
## - 터미널을 통한 메뉴 출력 -> 사용자 선택
## - 사용자의 종료 입력 전까지 반복
## --------------------------------------------------------
## 사용자 정의 함수들
## --------------------------------------------------------
## 전역 변수 및 파일 미리 설정
FILE_NAME = './calc_history.txt'


## 메인 메뉴 출력 기능
def printMenu():
    '''
    ## 함수기능 : 메인메뉴 출력 기능
    ## 함수이름 : printMenu
    ## 매개변수 : 없음
    ## 결과반환 : 없음
    '''
    print(f'{"선택":-^10}')
    print(f'{"1. 입  력":^10}')
    print(f'{"2. 덧  셈":^10}')
    print(f'{"3. 곱  셈":^10}')
    print(f'{"4. 뺄  셈":^10}')
    print(f'{"5. 나눗셈":^8}')
    print(f'{"6. 기  록":^10}')
    print(f'{"0. 종  료":^10}')
    print(f'{"":-^12}')

# 연산에 사용될 데이터 2개 입력 받기 기능
def inputData():
    '''
    ## 함수기능 : 연산에 사용될 데이터 2개 입력 받기 기능
    ## 함수이름 : inputData
    ## 매개변수 : 없음
    ## 결과반환 : 입력 받은 2개 데이터
    '''
    return map(int, input("2개 정수 입력(예시: 30 2) : ").split())

# 덧셈 결과 출력하는 함수
def pluse():
    '''
    ## 함수기능 : 덧셈 결과 출력하는 함수
    ## 함수이름 : pulse
    ## 매개변수 : 없음
    ## 결과반환 : 없음
    '''
    # 전역변수 수정 선언
    global n1, n2
    # 결과 화면 출력
    print(f'{n1} + {n2} = {n1 + n2}')   ## <- 여기선 기존 값으로 계산하고
    # 결과 파일 저장
    saveHistory(f'{n1} + {n2} = {n1+n2}')
    # 전역변수 초기화
    n1, n2 = None, None                 ## <- 여기서 값 초기화 진행

## 연산 결과 저장 함수
def saveHistory(data, filename=FILE_NAME ):
    '''
    ## 함수기능 : 연산 결과 저장 함수
    ## 함수이름 : saveHistory
    ## 매개변수 : filename - 경로포함한 파일명 [기] ./calc_history.txt
    ##           data     - 파일에 저장할 데이터
    ## 결과반환 : 파일에 쓴 문자 개수 반환
    '''
    with open(filename, mode='a', encoding='utf-8') as F:
        F.write(data+'\n')

## 연산 결과 이력 출력 함수
def printHistory(filename=FILE_NAME):
    '''
    ## 함수기능 : 연산 결과 이력 출력 함수
    ## 함수이름 : printHistory
    ## 매개변수 : filename - 경로포함한 파일명 [기] ./calc_history.txt
    ## 결과반환 : 화면 출력으로 반환 없음
    '''
    with open(filename, mode='r', encoding='utf-8') as F:
        lines = F.readlines()
    
    ## 최근 연산 결과를 위에 출력하기 위해서 뒤집음
    lines.reverse()
    for line in lines:
        print(line.strip('\n'))


## --------------------------------------------------------
## 프로그램 구동 부분
## --------------------------------------------------------
print("계산기 프로그램 시작")

n1, n2 = None, None
while True:
    # 메뉴 출력
    printMenu()
    cmd = input("선택 번호 입력 : ").strip()

    # 종료 체크 및 처리
    if cmd in ['0', 'O', 'o']: break
    
    # 입력 함수 사용
    elif cmd == '1':
        n1, n2 = inputData()

    # 덧셈 함수 사용 <- 사용 후 초기화 해줘야됨
    elif cmd == '2':
        if n1 != None and n2 != None:
            pluse()

    elif cmd == '3':
        pass
    elif cmd == '4':
        pass
    elif cmd == '5':
        pass

    # 기록
    elif cmd == '6':
        printHistory()

    # 잘못 입력했을 때
    else :
        print("존재하지 않는 항목입니다.")

print("계산기 프로그램 종료")