## --------------------------------------------------------
## Python GUI Programming - TKinter
## --------------------------------------------------------
## 모듈 로딩
## --------------------------------------------------------
from tkinter import *

## - 윈도우 창 인스턴스 생성
mainWin = Tk()

## - 윈도우 창에 설정
mainWin.title("My App")                     ## 윈도우 창 이름
mainWin.geometry('1000x200+100+100')        ## 창 크기와 위치 설정  (w x h + x + y) => (가로x세로+x좌표+y좌표)
mainWin.resizable(False, False)             ## 가로 세로 크기 변경 고정 유뮤
#  mainWin.resizable(True, True)

## - 윈도우에서 발생하는 사용자 이벤트 수신
## - 윈도우 종료전까지 동작
mainWin.mainloop()