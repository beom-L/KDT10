## --------------------------------------------------------
## Python GUI Programming - TKinter
## ** Label Widget : 텍스트, 이미지 출력 UI 요소
## --------------------------------------------------------
## 모듈 로딩
## --------------------------------------------------------
from tkinter import *
import os                         ## 이미지 경로 관련 모듈
from PIL import Image, ImageTk    ## TK 미지원 이미지 처리 위한 모듈

## --------------------------------------------------------
## - 사용자 정의 함수
## --------------------------------------------------------
## - 함수기능 : 이미지 데이터에서 TKinter용 이미지 추출 후 반환
## - 함수이름 : get_img
## - 매개변수 : imgpath         - 이미지명 포함 경로
## - 반환결과 : TKinter용 이미지 데이터
## --------------------------------------------------------
def get_img(imgpath):
    ## => 지원&미지원 이미지 처리
    _, ext = os.path.splitext(imgpath)            ## 이름이랑 확장자로 나와서 이름은 버림
    if ext in ['.png', 'bmp', 'gif', '.ppm', '.pgm']:
        return PhotoImage(file=imgpath)
    else:
        ## 순수 이미지 데이터 추출
        img = Image.open(imgpath)
        ## 이미지 데이터 전달
        return ImageTk.PhotoImage(image = img)

## --------------------------------------------------------
## - 윈도우 관련
## --------------------------------------------------------
## - 윈도우 창 인스턴스 생성
mainWin = Tk()

## - 윈도우 창에 설정
mainWin.title("My App")                     ## 윈도우 창 이름
mainWin.geometry('1000x200+100+100')        ## 창 크기와 위치 설정  (w x h + x + y) => (가로x세로+x좌표+y좌표)
mainWin.resizable(True, True)             ## 가로 세로 크기 변경 고정 유뮤

## --------------------------------------------------------
## - 윈도우에 배치될 UI 요소들 - Image Lable 요소
## - 지원 이미지 확장자 : .png, .bmp, .gif, .ppm, .pgm
## - 미지원 이미지 경우 : 로우 데이터 추출 필요 => conda install pillow   => import PIL
## --------------------------------------------------------
## 인스턴스 생성
## => 지원 이미지 : png, bmp, gif, ppm, prn
IMG_FILE1 = '../Image/apple47.jpg'
IMG_FILE2 = '../Image/apple76.png'
IMG_FILE3 = '../Image/text.png'


img1 = get_img(IMG_FILE1)
img2 = get_img(IMG_FILE2)
img3 = get_img(IMG_FILE3)
## - 이미지 라벨 인스턴스 생성
imgLB1 = Label(mainWin, image=img1)  
imgLB2 = Label(mainWin, image=img2)  
imgLB3 = Label(mainWin, image=img3)  


## UI 인스턴스 윈도우에 배치
imgLB1.pack(side='left')
imgLB2.pack()
imgLB3.pack(side='right')


## --------------------------------------------------------
## - 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------
## - 윈도우 종료전까지 동작
mainWin.mainloop()