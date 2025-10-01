## [1] homework.txt, message.txt 파일 읽어서 출력
FILE_home = './homework.txt'
FILE_mess = './message.txt'

with open(FILE_home, mode='r', encoding='utf-8') as hFILE:
    print(f'homework 파일 출력 : \n {hFILE.read()}')

with open(FILE_mess, mode='r', encoding='ANSI') as mFILE:
    print(f'\nhomework 파일 출력 : \n {mFILE.read()}')


## [2] data.txt 복사해서 data_copy.txt를 생성
FILE_data = './data.txt'

with open(FILE_data, mode='r',encoding='utf-8') as dFILE:
    file = dFILE.readlines()
    new = open('./data_copy.txt', mode='w',encoding='utf-8')
    for f in file:
        new.write(f)


## ---------------------------------------------------------------
## 강사님
## [1]
FILE_home = './homework.txt'
FILE_mess = './message.txt'
FILE_data = './data.txt'
FILE_copy = './data_copy.txt'

def print_file(filename, encode='utf-8'):                        ## <= 이렇게 함수로 만들었음
    with open(filename, mode='r', encoding=encode) as f:
        print(f.read())

print_file(FILE_home)
print_file(FILE_mess, 'ansi')


## [2]
def copy_file(originF, copyF, encode='utf-8'):
    ## 원본 파일 열기
    with open(originF, mode='r', encoding=encode) as rf:
        ## 새로운 파일 열기
        with open(copyF, mode='w', encoding=encode) as wf:
            ## 원본 내용 읽어서 새로운 파일에 쓰기
            wf.write(rf.read())

# 함수호출
copy_file(FILE_data,FILE_copy)