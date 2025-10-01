## --------------------------------------------------------------------------------
## 파일 입출력
## - 퍼알 위치 관련 메서드
##              * seek( offset ) : 파일 포인터의 위치 설정
##              * tell()         : 현재 파일 포인터의 위치 알려줌
## - 파일 속성 관련 변수
##              * closed : 닫혔는지 여부 True/False
##              * mode   : 현재 파일의 모드
##              * name   : 현재 파일 이름
## --------------------------------------------------------------------------------
## 파일 설정
F_NAME = './exam01/data.txt'

with open(F_NAME, mode='r', encoding='utf-8') as F:
    ## 처음 ~ 끝까지 읽기
    while True:
        line = F.readline()
        print(line)
        if not len(line): break
        print(f'현재 파일 포인트 위치 : {F.tell()}')

    ## 한번 더 읽기 
    print('-----------------------------------------')
    F.seek(0)            # <------------- 이게 file point를 처음으로 돌리는거임
    while True:
        line = F.readline()
        print(line)
        if not len(line): break
        print(f'현재 파일 포인트 위치 : {F.tell()}')   # <----- tell은 현재 위치 말해주는 것


## => 현재 파일의 속성 및 상태
print(f'F.closed : {F.closed}')
print(f'F.mode   : {F.mode}')
print(f'F.name   : {F.name}')