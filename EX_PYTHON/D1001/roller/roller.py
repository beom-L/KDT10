## ----------------------------------------------------------
##                  음식 추천 돌림판
## [ 입력 음식 무작위로 추천 [ex) 치킨, 피자, 햄버거, ...] ]
## 1. 음식 입력
## 2. 룰렛 돌리기
## 3. [결과가 마음에 안들면 선택!] 음식 다시 돌리기. 1회 가능.
## 4. 추첨 기록 확인
## 5. 음식 추천 (첫 실행시 불가능)
## X. 종료
## ----------------------------------------------------------
import random

FILEroller = './roller.txt'
FILENoDel = './noDel.txt'  ## 초기화 되지 않는 파일

n = 0

## 메인 메뉴 출력 기능
def printMenu():
    '''
    ## 함수기능 : 메인메뉴 출력 기능
    ## 함수이름 : printMenu
    ## 매개변수 : 없음
    ## 결과반환 : 없음
    '''
    print(f'{"선택":-^10}')
    print(f'{"1. 음식 입력 ":^10}')
    print(f'{"2. 룰렛 돌리기":^10}')
    print(f'{"3. 음식 다시 돌리기 (1회 사용 가능)":<10}')
    print(f'{"   [결과가 마음에 안들면 선택 !]":<10}')
    print(f'{"4. 기록 확인":<10}')
    print(f'{"5. 음식 추천":^8}')
    print(f'{"X. 종  료":<10}')
    print(f'{"":-^12}')

## 1. 음식 입력 받아서 roller과 noDel에 저장
def inputFood():
    '''
    ## 함수기능 : 음식 입력 받아서 roller에 저장
    ## 함수이름 : inputFood
    ## 매개변수 : 없음
    ## 결과반환 : 없음
    '''
    foods = input("음식 입력(ex] 햄버거 피자 치킨 ...) : ").split()
    with open(FILEroller, mode = 'w', encoding='utf-8') as F:  ## <- 지우고 새로 작성. 즉 최종 작성 음식만 남아있음
        for food in foods:
            F.write(food+' ')
        F.write('\n')


## 2. 입력 받은 음식 random 돌리기 + 3. 다시 돌리기 (1회 가능)
def foodRandom(again=False, FILENAME=FILEroller):
    '''
    ## 함수기능 : 입력 받은 음식 random 돌리기
    ## 함수이름 : foodRandom
    ## 매개변수 : [기] 최근 음식 입력 돼있는 txt 파일
    ## 결과반환 : 무작위 선택된 음식 반환
    '''
    global n

    with open(FILENAME, mode = 'r', encoding='utf-8') as F:
        
        nowFood = F.readlines()
        result = nowFood[0].rstrip('\n').split()
        random_result = random.choice(result)

        with open(FILENoDel, mode = 'w', encoding='utf-8') as F:  ## <- 지우고 새로 작성. 즉 최종 무작위 선택 음식만 남아있음
            F.write(random_result+'\n')

        if again == True and n < 1: ## 1번 이하로 돌리는 상황이면
            n += 1
            return random_result

        elif again == True and n >= 1:  ## 1
            return None
        
        elif again == False : 
            return random_result


## 3. 기록 확인
def againReturn():
    '''
    ## 함수기능 : 선택 된 음식 기록 확인
    ## 함수이름 : againReturn
    ## 매개변수 : [기] 최근 음식 입력 돼있는 txt 파일
    ## 결과반환 : 무작위 선택된 음식 반환
    '''


while True:
    ## 기본 메뉴 출력
    printMenu()
    # 프로그램 시작 시 번호 선택
    cho = input('선택 번호 입력 : ').strip()
    # X 입력 시. 즉시 종료
    if cho in ['x', 'X']:
        break
    # 1. 음식 입력
    elif cho == '1':
        inputFood()
    # 2. 룰렛 돌리기
    elif cho == '2':
        print(f'룰렛 결과 : ""{foodRandom()}""')
    # 3. 다시 돌리기 (1회만 가능) -> 혹시 1번이 선택되면 초기화 하는 작업 필요함
    elif cho == '3':
        result = foodRandom(again=True)
        if  result != None:
            print(f'룰렛 결과 : ""{foodRandom(again=True)}""')
        else :
            print('기회를 모두 소진했습니다')

        
    # 4. 기록 확인
    elif cho == '4':
        pass

    # 음식 추천 -> 이전에 text에 작성된 내용이 없으면 X
    elif cho == '5':
        pass
    else:
        print("잘못 입력하셨습니다.")

print('프로그램 종료')