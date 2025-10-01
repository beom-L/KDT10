## -------------------------------------------------------------------------
## 파일 입출력 - [1] 파일 쓰기
## -------------------------------------------------------------------------
## - 내장함수 : open()
##   * filepath+filename : 존재하면 내용을 지우고 쓰기, 없으면 생성 [mode='w']
##   * mode              : 파일 작업 모드 설정
##                         'w' - 기존 내용 삭제, 새롭게 쓰기
##                         'a' - 기존 내용에 추가 (append의 약자임)
##   * encoding          : 기계어 변환(코드화)위한 기준 테이블
##   * 반환값             : 파일 접근 가능한 객체/주소
## -------------------------------------------------------------------------
## 전역변수 정의
## -------------------------------------------------------------------------
FILE_NAME = './send_msg.txt'


## -------------------------------------------------------------------------
## 파일에 쓰기 기능 => whit ~ as
## -------------------------------------------------------------------------
## [1] 파일 열기 - mode = 'w' : 기존 내용 삭제 후 쓰기
## - 영어 외의 언어를 입력시, encoding 지정해야함.
with open(FILE_NAME, mode='w', encoding='utf-8') as textF:

    ## [2] 파일에 쓰기 => 데이터 미리 지정
    data = ['Good Luck', 'Happy New Year', '2025!!', '오늘은 좋은 날']
    data = [d+'\n' for d in data]

    # 줄바꿈 문자 없음 -> 전달되는 데이터에 줄바꿈 문자 추가 필요할 수 있음
    textF.writelines(data)

FILE_NAME = './send_msg2.txt'

## [1] 파일 열기 - mode = 'a' : 기존 내용 아래에 내용 추가하기
## - 영어 외의 언어를 입력시, encoding 지정해야함.
with open(FILE_NAME, mode='a', encoding='utf-8') as textF:

    data = ['Good Luck', 'Happy New Year', '2025!!', '오늘은 좋은 날']
    data = [d+'\n' for d in data]

    # 줄바꿈 문자 없음 -> 전달되는 데이터에 줄바꿈 문자 추가 필요할 수 있음
    textF.writelines(data)


FILE_NAME = './send_msg3.txt'

## [1] 파일 열기 - mode = 'x' : 기존 존재 파일이면 ERROR 발생
## - 영어 외의 언어를 입력시, encoding 지정해야함.
with open(FILE_NAME, mode='x', encoding='utf-8') as textF:

    data = ['Good Luck', 'Happy New Year', '2025!!', '오늘은 좋은 날']
    data = [d+'\n' for d in data]

    # 줄바꿈 문자 없음 -> 전달되는 데이터에 줄바꿈 문자 추가 필요할 수 있음
    textF.writelines(data)