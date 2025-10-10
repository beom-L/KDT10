## ----------------------------------------------------------
##                  음식 추천 돌림판
## [ 입력 음식 무작위로 추천 [ex) 치킨, 피자, 햄버거, ...] ]
## 1. 음식 입력
## 2. 룰렛 돌리기
## 3. [결과가 마음에 안들면 선택!] 음식 다시 돌리기. 1회 가능.
## 4. 추첨 기록 확인 
## 5. 음식 추천 (첫 실행시 불가능)
## D. 기록 지우기
## X. 종료
## ----------------------------------------------------------
import random

FILEroller = './roller.txt'  ## 현재 입력한 음식만 저장됨
FILENoDel = './noDel.txt'    ## 마지막 룰렛 결과만 저장됨 + 초기화 되지 않는 파일
n_2, n_3 = 0, 0              ## 2번/3번을 위한 변수        

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
    print(f'{"D. 기록 지우기":<10}')
    print(f'{"X. 종  료":<10}')
    print(f'{"":-^12}')

## D. 파일 내용 모두 지우기
def DelAll(FILE=FILENoDel):
    '''
    ## 함수기능 : 기록 지우기
    ## 함수이름 : DelAll
    ## 매개변수 : [기] FILENoDel
    ## 결과반환 : 없음
    '''
    with open(FILE, mode='w',encoding='utf-8') as F:
        pass
    print('내용을 모두 지웠습니다.')

## 1. 음식 입력 받아서 roller과 noDel에 저장
def inputFood():
    '''
    ## 함수기능 : 음식 입력 받아서 roller에 저장
    ## 함수이름 : inputFood
    ## 매개변수 : 없음
    ## 결과반환 : 없음
    '''
    global n_2, n_3
    
    foods = input("음식 입력(ex] 햄버거 피자 치킨 ...) : ").split()
    with open(FILEroller, mode = 'w', encoding='utf-8') as F:  ## <- 지우고 새로 작성. 즉 최종 작성 음식만 남아있음
        for food in foods:
            F.write(food+' ')
        # F.write(' '.join(foods) + '\n') 

    n_2, n_3 = 1, 0 ## 만약 다시 입력하면 2번 3번 초기화

## 2. 입력 받은 음식 random 돌리기 + 3. 다시 돌리기 (1회 가능)
def foodRandom(again=False, FILENAME=FILEroller):
    '''
    ## 함수기능 : 입력 받은 음식 random 돌리기
    ## 함수이름 : foodRandom
    ## 매개변수 : [기] 최근 음식 입력 돼있는 txt 파일
    ## 결과반환 : 무작위 선택된 음식 반환
    '''
    
    global n_2, n_3

    with open(FILENAME, mode = 'r', encoding='utf-8') as F:
        nowFood = F.readlines()                  # print(nowFood) # ['햄버거 피자 치킨 ']
        result = nowFood[0].split()              # print(result) # ['햄버거', '피자', '치킨']
        random_result = random.choice(result)    # print(random_result) # 햄버거

        ## Nodel 파일에 지속적으로 update 하기
        with open(FILENoDel, mode = 'a', encoding='utf-8') as F:  ## <- 지워지지 않는 파일(nodel)에 append하기
            for food in result:
                F.write(food+' ')                       # 햄버거 피자 치킨 
            F.write('\n')                               # [단 내리기]
            F.write(f'결과 = '+ random_result +'\n')    # 결과 = 햄버거 + [단 내리기]

        if n_2 == 0:
            if again:
                return '다시 돌릴 항목이 없습니다.'
            elif again == False:
                return '1번 선택 후, 음식을 입력해 주십시오'
        # if again and n_2 == 0 :              ## 시작하자 마자 3번 입력한 경우
        #     return '다시 돌릴 항목이 없습니다.'

        elif again == False and n_2 == 1 :           ## 일반적인 룰렛 돌리기. (처음 한번만 가능)
            n_2 += 1
            return random_result

        elif again and n_3 < 1:              ## 3번 입력한 경우 + 처음 클릭한거임.
            n_3 += 1
            return random_result                     ## 다시 돌린 결과값 반환
        

## 4. 기록 확인
def RecordCheck():
    '''
    ## 함수기능 : 선택 된 음식 기록 확인
    ## 함수이름 : RecordCheck
    ## 매개변수 : [기] 최근 음식 입력 돼있는 txt 파일
    ## 결과반환 : 무작위 선택된 음식 반환
    '''
    with open(FILENoDel, mode='r', encoding='utf-8') as F:
        lines = F.readlines()
    
    lines.reverse()
    for line in lines:
        print(line.strip('\n'))
    

## 5. 음식 추천
def foodRecommend(TEXTNAME=FILENoDel):
    '''
    ## 함수기능 : 기록된 기록에서 음식 무작위 음식 추천
    ## 함수이름 : foodRecommend
    ## 매개변수 : [기] 음식 입력 돼있는 txt 파일
    ## 결과반환 : 무작위 선택된 추천 음식 반환    
    '''
    try:
        with open(TEXTNAME, mode='r',encoding='utf-8') as F:
            lines = F.readlines()
            result = []
            for line in lines[::2]:
                # line[-1].rstrip('\n') ## \n은 공백으로 분류
                line = line.split()
                for l in line:
                    result.append(l)
            print(f'""{random.choice(result)}"" 추천 드립니다 !')
    except Exception as e:
        print('기록이 없어서 추천이 불가합니다.')
        

while True:
    ## 기본 메뉴 출력
    printMenu()
    # 프로그램 시작 시 번호 선택
    cho = input('선택 번호 입력 : ').strip()
    # X 입력 시. 즉시 종료
    if cho in ['x', 'X']:
        break
    elif cho == 'D':
        DelAll()
    # 1. 음식 입력
    elif cho == '1':
        inputFood()
    # 2. 룰렛 돌리기
    elif cho == '2':
        print(f'룰렛 결과 : ""{foodRandom()}""')  if n_2 <= 1 else print('3번. 룰렛 다시 돌리기를 사용해 주십시오')
        
    # 3. 다시 돌리기 (1회만 가능) -> 혹시 1번이 선택되면 초기화 하는 작업 필요함
    elif cho == '3':
        print(f'룰렛 결과 : ""{foodRandom(again=True)}""') if n_3 == 0 else print('기회가 모두 소진되었습니다.')
        
    # 4. 기록 확인
    elif cho == '4':
        print('[ 기  록 ]')
        RecordCheck()

    # 5. 음식 추천 -> 이전에 text에 작성된 내용이 없으면 X
    elif cho == '5':
        foodRecommend()
    
    # 그 외
    else:
        print("잘못 입력하셨습니다.")

print('프로그램 종료')